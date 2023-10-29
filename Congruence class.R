library(castor)
library(ape)
library(tidyverse)
library(phytools)


#-############################################################################-#
# Construction of congruence class problem ----
#-############################################################################-#

set.seed(42)

ncc <- 1000 # Number of members in the congruence class
ngrid <- 1000 # Grid size of the "continuous" rates
maxpoints <- 4 # Maximal number of change points
xmax <- 10 # Root time
npoints <- sample(0:maxpoints, ncc, replace = TRUE) # number of change points for the specific realisations
npoints[1] <- 4

lambda_p <- rnorm(npoints[1] + 2, 0.1, 0.01) # pulled birth rate
r_p <- rnorm(npoints[1] + 2, 0.6, 0.05) # pulled diversification rate
psi_p <- rnorm(npoints[1] + 2, 1, 0.01) # pulled sampling rate

# Model with the above values
m_pulled <- simulate_deterministic_hbds(age_grid = c(0, sort(sample(1:(xmax - 1), npoints[1])), xmax),
                                        requested_ages = seq(0, 10, length.out = ngrid),
                                        LTT0 = 1,
                                        age0 = 10,
                                        lambda = lambda_p,
                                        mu = r_p,
                                        psi = psi_p,
                                        kappa = rep(0, times = (npoints[1] + 2)),
                                        splines_degree = 3)

lambda_pulled_cc <- m_pulled$lambda
psi_pulled_cc <- m_pulled$psi
r_pulled_cc <- m_pulled$mu

cpoints <- lambda <- mu <- psi <- m <- list()

i <- 1
while(i <= ncc){
  cpoints[[i]] <- sort(sample(1:(xmax - 1), npoints[i])) # values of change points for realisation i
  
  psipsi <- rnorm(npoints[i] + 2, 0.1, 0.01)
  psi[[i]] <- simulate_deterministic_hbds(age_grid = c(0, sort(sample(1:(xmax - 1), npoints[i])), xmax),
                                          requested_ages = seq(0, 10, length.out = ngrid),
                                          LTT0 = 1,
                                          age0 = 10,
                                          lambda = rep(1, times = npoints[i] + 2),
                                          mu = rep(1, times = npoints[i] + 2),
                                          psi = psipsi,
                                          kappa = rep(0, times = (npoints[i] + 2)),
                                          splines_degree = 3)$psi
  lambda[[i]] <- lambda_pulled_cc * psi_pulled_cc / psi[[i]]
  mu[[i]] <- lambda[[i]] - r_pulled_cc - psi[[i]] + 1 / lambda[[i]] * (c((lambda[[i]][2] - lambda[[i]][1]) * (xmax / ngrid), (lambda[[i]][-1] - lambda[[i]][-ngrid]) * (xmax / ngrid)))
  
  # Model with the above values
  m[[i]] <- simulate_deterministic_hbds(age_grid = seq(0, xmax, length.out = ngrid),
                                        requested_ages = seq(0, xmax, length.out = ngrid),
                                        LTT0 = 1,
                                        age0 = xmax,
                                        lambda = lambda[[i]],
                                        mu = mu[[i]],
                                        psi = psi[[i]],
                                        kappa = rep(0, times = ngrid),
                                        splines_degree = 3)
  
  Nsamples <- 1; Ssamples <- 0
  for (j in 1:ngrid){
    Nsamples <- Nsamples + (m[[i]]$lambda[j] - m[[i]]$mu[j] - m[[i]]$psi[j]) * Nsamples * (xmax / ngrid) # expected number of samples
    Ssamples <- Ssamples + m[[i]]$psi[j] * Nsamples * (xmax / ngrid) # cumulatively sample individuals
  }
  
  # Filter sample sizes that are appropriate for the tree inference (20 and 100). In addition only use models with positive rates.
  if ((sum(m[[i]]$lambda < 0) > 0) || (sum(m[[i]]$mu < 0) > 0) || (sum(m[[i]]$psi < 0) > 0) || (Ssamples >= 100) || (Ssamples <= 20)){
    m <- m[-i]
  }
  else{
    cat(paste(i, "# Samples:", Ssamples), sep = "\n")
    i <- i + 1
  }
}


##-------------------------##
## Skyline approximation ----
##-------------------------##

skyline_interval_means <- model_from_skyline <- m_pwconst <- list()
changeAges <- c(2, 4, 6, 8, Inf) # interval boundaries

# Intervals for skyline approximation
skyline_intervals <- tibble(age = m[[1]]$ages) %>%
  rowwise() %>%
  mutate(interval = min(which(changeAges > age)))

for (i in 1:ncc){
  
  # Values of rates for all the intervals
  skyline_interval_means[[i]] <- skyline_intervals %>%  
    add_column(birth = m[[i]]$lambda) %>%
    add_column(death = m[[i]]$mu) %>%
    add_column(samp = m[[i]]$psi) %>%
    pivot_longer(cols = c("birth", "death", "samp"), names_to = "var",
                 values_to = "val") %>%
    group_by(interval, var) %>%
    summarize(val = mean(val))
  
  # Function that converts rates over intervals into stepwise constant models
  model_from_skyline[[i]] <- function(skyline){
    tmp <- skyline %>% left_join(skyline_intervals)
    m_skyline <- simulate_deterministic_hbds(age_grid = skyline_intervals$age,
                                             requested_ages = skyline_intervals$age,
                                             lambda = (tmp %>% filter(var == "birth"))$val,
                                             mu = (tmp %>% filter(var == "death"))$val,
                                             psi = (tmp %>% filter(var == "samp"))$val,
                                             LTT0 = 1,
                                             age0 = xmax,
                                             splines_degree = 1)
    return(m_skyline)
  }
  
  # Construct model with rates from above
  m_pwconst[[i]] <- model_from_skyline[[i]](skyline_interval_means[[i]])
}



############################################
# Likelihood calculation using the dLTT ----
############################################

lambda_pulled_pw <- psi_pulled_pw <- list()

for (i in 1:ncc){
  lambda_pulled_pw[[i]] <- m_pwconst[[i]]$lambda * (1 - m_pwconst[[i]]$Pmissing)
  psi_pulled_pw[[i]] <- m_pwconst[[i]]$psi / (1 - m_pwconst[[i]]$Pmissing)
}


lik_dLTT_truth <- perc_smaller_truth <- perc_further_away <- c(); lik_dLTT <- list()

for (truth in 1:ncc){
  p_nb <- p_nd <- 0
  for (i in 2:ngrid){
    dt <- (xmax / ngrid)
    k <- m[[truth]]$LTT[i]
    nb <- dt * k * lambda_pulled_cc[i]
    nd <- dt * k * psi_pulled_cc[i]
    p_nb <- p_nb - nb + log((nb)^(nb)) - log(factorial(floor(nb)))
    p_nd <- p_nd - nd + log((nd)^(nd)) -  log(factorial(floor(nd)))
  }
  
  lik_dLTT_truth[truth] <- p_nb + p_nd

  for (j in 1:ncc){
    p_nb <- p_nd <- 0
    for (i in 2:ngrid){
      dt <- (xmax / ngrid)
      k <- m[[truth]]$LTT[i]
      nb <- dt * k * lambda_pulled_cc[i]
      nd <- dt * k * psi_pulled_cc[i]
      p_nb <- p_nb - dt * k * lambda_pulled_pw[[j]][i] + log((dt * k * lambda_pulled_pw[[j]][i])^(nb)) - log(factorial(floor(nb)))
      p_nd <- p_nd - dt * k * psi_pulled_pw[[j]][i] + log((dt * k * psi_pulled_pw[[j]][i])^(nd)) -  log(factorial(floor(nd)))
    }
    if (j == 1){
      lik_dLTT[[truth]] <- p_nb + p_nd
    }
    else{
      lik_dLTT[[truth]][j] <- p_nb + p_nd
    }      
    cat(paste(truth, j, sep = " "), sep = "\n")
  }

  # Percentage of likelihoods (piecewise approximations) smaller than the "truth"
  perc_smaller_truth[truth] <- mean(lik_dLTT_truth[truth] - lik_dLTT[[truth]] > 0)
  
  # Percentage of likelihoods that are further away from the "truth" than its optimal piecewise approximation
  perc_further_away[truth] <- mean(lik_dLTT[[truth]][truth] - lik_dLTT[[truth]][-truth] > 0)
}


# Save the percentages to disc
write(perc_smaller_truth, "perc_smaller_truth.txt", ncolumns = length(perc_smaller_truth), sep = "\t")
write(perc_further_away, "perc_further_away.txt", ncolumns = length(perc_further_away), sep = "\t")

# Save likelihoods to disc
write(lik_dLTT_truth, "lik_dLTT_truth.txt", ncolumns = length(lik_dLTT_truth), sep = "\t")
for (i in 1:ncc){
  write(lik_dLTT[[i]], paste("lik_dLTT", i, ".txt", sep = ""), ncolumns = length(lik_dLTT[[i]]), sep = "\t")
}


# Read likelihoods from files
lik_dLTT_truth <- scan("lik_dLTT_truth.txt")
lik_dLTT <- list()

for (i in 1:ncc){
  lik_dLTT[[i]] <- scan(paste("lik_dLTT", i, ".txt", sep = ""))
}

# Read the percentages from files
perc_smaller_truth <- scan("perc_smaller_truth.txt")
perc_further_away <- scan("perc_further_away.txt")


# Distribution of largest likelihood amongst the piecewise approximations
max_pw <- c()

for (i in 1:ncc){
  max_pw[i] <- which.max(lik_dLTT[[i]])
}

table(max_pw) # 100% position 325


# Percentage of likelihoods (piecewise approximations) smaller than the "truth" (100%)
mean(perc_smaller_truth)

# Distribution of percentage of likelihoods that are further away from the "truth" than its optimal piecewise approximation
hist(perc_further_away, breaks = 20, xlab = "Percentage",
     main = "Distribution of likelihoods smaller than the \"true\" optimal approximation")
