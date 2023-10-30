# import libraries needed
library(ggplot2)
library(plyr)
library(dplyr)
library(readxl)
library(stringr)
library(gtools)


# define directories where files are located
server_dir <- "N:/bowiss/Alle/Projekte/morphologie_db/Daten/Daten_SPA_Gradient_Schweiz/Zivildienst_Emil_Majdandzic_2023/"
site_dir <- paste0(server_dir, "/Konvertierung_zu_WP4C/Soil_water_potential_korrigiert/")
heightfile <- paste0(server_dir, "Gruppierung_Baumarten/data/Bestandesoberhoehe_44_sites.xlsx")
odir <- "N:/lwf/3.2_Bodenwasser/Projekte_bowa/2018_2_Drought2018_SOILWATER/_single_site_calibration/2023_Oberboden/output/"
dir_in <- paste0(server_dir, "Konvertierung_zu_WP4C/Soil_water_potential_korrigiert/")
dir_out <- paste0(server_dir, "Gruppierung_Baumarten/3_Buche1234_Eiche/")


# change plotting colours for case with bu1, bu2, bu3, bu4, ei
custom_colours <- function(x){
  ## INPUT
  # string of group name
  
  ## OUTPUT
  # colour of the group from INPUT
  
  case_when(
    x == "Buche - sehr hoch" ~ "blue",
    x == "Buche - hoch" ~ "deepskyblue",
    x == "Buche - mittelhoch" ~ "forestgreen",
    x == "Übergang Buche-Eiche" ~ "chartreuse1",
    x == "Flaumeiche" ~ "red"
  )
}


# plotting function for time series of soil water potential
plot_fct <- function(data, groups, depths, stderr = TRUE, filetitle = "Allsites", mov_avg_len = 1){
  
  ## INPUT
  # data: dictionary with key = site number and value = site name
  # groups: list of group names for each site
  # depths: list of depths
  # stderr: boolean defining if the standard error is to be plotted (default: standard error plotted)
  # filetitle: string of output file title (default: all sites are used)
  # mov_avg_len: length of moving average interval (default: no moving average)
  
  ## OUTPUT
  # plot of soil water potential time series (moving average of median) grouped by "groups" from 2015- for the depths given
  
  depths_rev <- sort(depths, decreasing = TRUE)
  
  height_file <- read_excel(heightfile)[-1,c(2,22)]
  names(height_file) <- c("PROFIL_NR", "HEIGHT")
  
  dat <- tibble()
  present_PROFIL_NR <- c()
  
  for (i in 1:length(data)){
    
    # print progression
    print(paste0("Reading in ", names(data)[i], "_", data[[i]], ".xlsx ", i, "/",
                 length(data), " ..."))
    
    dat1 <- read_excel(paste0(
      dir_in, names(data)[i], "_", data[[i]], ".xlsx"))[, c("PROFIL_NR", "NAME",
                                                            "MEAS_DATE", "VALUE",
                                                            "CORRECTION_WP4C")]
    
    # use value at 12:00 and values such that the moving average can be calculated from 01.01.2015
    dat1 <- dat1[format(dat1$MEAS_DATE, "%H") == "12",]
    dat1 <- dat1[dat1$MEAS_DATE >= as.Date("2015-01-01") - ceiling(mov_avg_len/2),]
    
    # add column for forest type, profile number with depth and tree height
    dat1$GROUP <- groups[i]
    dat1$PROFIL_DEPTH <- paste0(dat1$PROFIL_NR, "_", gsub("\\D", "", dat1$NAME))
    dat1$HEIGHT <- round(height_file[height_file$PROFIL_NR == names(data)[i],]$HEIGHT)
    
    # extract only data for depths needed 
    df <- tibble()
    for (depth in depths_rev){
      df <- dat1[dat1$NAME == paste0("22 Soil water potential mean ", depth, " cm"),]
      if (nrow(df) != 0){
        present_PROFIL_NR <- c(present_PROFIL_NR, dat1$PROFIL_NR[1])      
        break
      }
    }
    dat <- rbind(dat, df)
  }
  
  # print progression
  print("Adjusting data ...")
  
  # clean data from NAs (-9999999) and artifacts
  dat <- dat[!(dat$CORRECTION_WP4C == -9999999),]
  dat <- dat[!(apply(is.na(dat), 1, sum)),]
  
  # adjust date format to show year/month/day
  dat$MEAS_DATE <- as.Date(dat$MEAS_DATE, format = "%y/%m/%d")
  
  # compute moving average
  i <- 1
  for (item in names(data)){
    if (item %in% present_PROFIL_NR){
      dat[dat$PROFIL_NR == item,]$CORRECTION_WP4C <- stats::filter(dat[dat$PROFIL_NR == item,]$CORRECTION_WP4C,
                                                                   rep(1/mov_avg_len, mov_avg_len),
                                                                   sides = 2)
    }
    else{
      groups[i] <- NA
    }
    i <- i + 1
  }
  
  # combine data for every forest type group
  dat <- ddply(dat, c("GROUP", "MEAS_DATE"), summarise,
               MEDIAN = median(CORRECTION_WP4C),
               STDERR = ifelse(is.na(sd(CORRECTION_WP4C)), 0, sd(CORRECTION_WP4C) / sqrt(length(CORRECTION_WP4C))),
               COUNT = length(CORRECTION_WP4C),
               stderrMIN = ifelse(is.na(sd(CORRECTION_WP4C)), median(CORRECTION_WP4C),
                               median(CORRECTION_WP4C) - sd(CORRECTION_WP4C) / sqrt(length(CORRECTION_WP4C))),
               STDERRMAX = ifelse(is.na(sd(CORRECTION_WP4C)), median(CORRECTION_WP4C),
                               median(CORRECTION_WP4C) + sd(CORRECTION_WP4C) / sqrt(length(CORRECTION_WP4C))),
               MIN_HEIGHT = min(HEIGHT),
               MAX_HEIGHT = max(HEIGHT))
  
  # subset data to start from 01.01.2015
  dat <- dat[dat$MEAS_DATE >= "2015-01-01",]
  
  # values have to be in [-4000,0]
  dat$STDERRMAX <- ifelse(dat$STDERRMAX > 0, 0, dat$STDERRMAX)
  dat$STDERRMIN <- ifelse(dat$STDERRMIN < - 4000, -4000, dat$STDERRMIN)
  
  # construct legend containing group name, tree height interval and number of sites in group
  dat$Legende <- ""
  groups_new <- groups[!is.na(groups)]
  for (grp in unique(groups_new)){
    dat[dat$GROUP == grp,]$Legende <-
      paste0(grp, ", (", min(dat[dat$GROUP == grp,]$MIN_HEIGHT), "m, ",
             max(dat[dat$GROUP == grp,]$MAX_HEIGHT), "m), n=", sum(groups_new == grp))
  }
  dat$GROUP <- factor(dat$GROUP, levels = sort(unique(groups_new)))
  
  # construct colour of confidence interval
  dat$FILL_COLOUR <- custom_colours(dat$GROUP)
  
  # omit missing values
  dat <- dat[!is.na(dat$MEDIAN),]
  
  
  # make plot of soil water potential time series
  g <- ggplot(data = dat, aes(x = MEAS_DATE, y = MEDIAN, ymin = STDERRMIN,
                              ymax = STDERRMAX, fill = Legende,
                              color = Legende)) +

    ylim(min(dat$STDERRMIN), 0) +
    
    # mark winter / non-vegetative months (October-April)
    annotate("rect", xmin = as.Date("2015-01-01"), xmax = as.Date("2015-04-30"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    annotate("rect", xmin = as.Date("2015-10-01"), xmax = as.Date("2016-04-30"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    annotate("rect", xmin = as.Date("2016-10-01"), xmax = as.Date("2017-04-30"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    annotate("rect", xmin = as.Date("2017-10-01"), xmax = as.Date("2018-04-30"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    annotate("rect", xmin = as.Date("2018-10-01"), xmax = as.Date("2019-04-30"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    annotate("rect", xmin = as.Date("2019-10-01"), xmax = as.Date("2020-04-30"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    annotate("rect", xmin = as.Date("2020-10-01"), xmax = as.Date("2021-04-30"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    annotate("rect", xmin = as.Date("2021-10-01"), xmax = as.Date("2022-04-30"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    annotate("rect", xmin = as.Date("2022-10-01"), xmax = as.Date("2022-12-31"),
             ymin = max(-8000, min(dat$STDERRMIN)),
             ymax = 0, alpha = 0.5, fill = "lightblue") +
    
    # plot median with colours by groups
    geom_line(aes(color = Legende), linewidth = 1.25) +
    
    geom_hline(yintercept = -2000) +
    geom_hline(yintercept = -4000) +
    labs(
      title = paste0("Time series of soil water potential moving average of ",
                     mov_avg_len, " days (", filetitle, ", ",
                     paste(depths, collapse = "/"), "cm)"),
      x = "Date",
      y = "SWP (median) in kPa at 12:00") +
    scale_x_date(date_breaks = "1 year", date_labels = "%Y") +
    theme_bw() +
    theme(
      plot.title = element_text(size = 40),
      axis.text = element_text(size = 22),
      axis.title = element_text(size = 30),
      legend.text = element_text(size = 22),
      legend.title = element_text(size = 30))
  
  # Legend for depths 20 and 50/70/80 with Buche1234_Eiche
  # THIS HAS TO BE ADJUSTED IF OTHER GROUPS ARE USED
  if (all(depths_rev == 20) | all(depths_rev == c(80, 70, 50))){
    g <- g + scale_color_manual(values = c("Buche - sehr hoch, (42m, 43m), n=2" = "blue",
                                           "Buche - hoch, (29m, 31m), n=2" = "deepskyblue",
                                           "Buche - mittelhoch, (23m, 26m), n=5" = "forestgreen",
                                           "Übergang Buche-Eiche, (14m, 22m), n=6" = "chartreuse1",
                                           "Flaumeiche, (8m, 14m), n=6" = "red"),
                                breaks = c("Buche - sehr hoch, (42m, 43m), n=2",
                                           "Buche - hoch, (29m, 31m), n=2",
                                           "Buche - mittelhoch, (23m, 26m), n=5",
                                           "Übergang Buche-Eiche, (14m, 22m), n=6",
                                           "Flaumeiche, (8m, 14m), n=6"))
  }
  
  # Legend for depths 140/150/160/180/190/200 with Buche1234_Eiche
  # THIS HAS TO BE ADJUSTED IF OTHER GROUPS ARE USED
  if (all(depths_rev == c(200, 190, 180, 160, 150, 140))){
    g <- g + scale_color_manual(values = c("Buche - sehr hoch, (42m, 42m), n=1" = "blue",
                                           "Buche - hoch, (29m, 29m), n=1" = "deepskyblue",
                                           "Buche - mittelhoch, (25m, 26m), n=3" = "forestgreen",
                                           "Übergang Buche-Eiche, (18m, 22m), n=3" = "chartreuse1",
                                           "Flaumeiche, (8m, 14m), n=4" = "red"),
                                breaks = c("Buche - sehr hoch, (42m, 42m), n=1",
                                           "Buche - hoch, (29m, 29m), n=1",
                                           "Buche - mittelhoch, (25m, 26m), n=3",
                                           "Übergang Buche-Eiche, (18m, 22m), n=3",
                                           "Flaumeiche, (8m, 14m), n=4"))
  }
  
  # standard error is plotted if specified
  if (stderr == TRUE){
    g <- g + geom_ribbon(alpha = 0.2, linewidth = 0, fill = dat$FILL_COLOUR)
  }
  
  # print progression
  print("Saving plot to disc ...")
  ggsave(paste0("SWP_", filetitle, "_Median_",
                ifelse(stderr == TRUE, "Stderr_", ""),
                paste(depths, collapse = "_"), "cm_", mov_avg_len, "dayavg.jpg"),
         plot = g, path = dir_out, scale = 1.7,
         width = 8000, height = 2000, units = "px", limitsize = FALSE)
}


# extract sites numbers and names
site_files <- sub("\\.xlsx$", "\\1", list.files(site_dir, pattern = "([0-9]+).*_*.xlsx"))
site_files <- mixedsort(site_files)

site_names <- sub("([0-9]+)", "", site_files)
site_names <- sub("_", "", site_names)

sites <- gsub("([0-9]+).*$", "\\1", site_files)

# construct dictionary of site number and name
allsites <- c()
for (i in 1:44){
  allsites[sites[i]] <- site_names[i]
}


# split data into different forest type groups
# NOT ALL 44 SITES ARE CONTAINED SINCE THERE ARE SIMILAR SITES
bu1_ind <- c("1133", "1178")
bu1 <- rep("Buche - sehr hoch", length(bu1_ind))

bu2_ind <- c("1565", "1568")
bu2 <- rep("Buche - hoch", length(bu2_ind))

bu3_ind <- c("898", "1566", "1570", "1572", "1723")
bu3 <- rep("Buche - mittelhoch", length(bu3_ind))

bu4_ind <- c("459", "1134", "1562", "1573", "1657", "1658")
bu4 <- rep("Übergang Buche-Eiche", length(bu4_ind))

ei_ind <- c("458", "1180", "1567", "1569", "1571", "1660")
ei <- rep("Flaumeiche", length(ei_ind))

fi1_ind <- c("125", "1558", "1559", "1560", "1555", "1724", "1725", "1726")
fi1 <- rep("fi1", length(fi1_ind))

foe1_ind <- c("1552", "1553", "1554")
foe1 <- rep("foe1", length(foe1_ind))

foe2_ind <- c("1556", "1557")
foe2 <- rep("foe2", length(foe2_ind))

foe3_ind <- c("108", "774", "890", "1122", "1574", "1575", "1563", "1564")
foe3 <- rep("foe3", length(foe3_ind))

ind <- c(bu1_ind, bu2_ind, bu3_ind, bu4_ind, ei_ind, fi1_ind, foe1_ind,
         foe2_ind, foe3_ind)
ind <- mixedorder(ind)
groups <- c(bu1, bu2, bu3, bu4, ei, fi1, foe1, foe2, foe3)
groups <- groups[ind]


# plotting ---------------------------------------------------------------------

## all sites

# plot with confidence interval
plot_fct(allsites, groups, 20, mov_avg_len = 28)
plot_fct(allsites, groups, c(50, 70, 80), mov_avg_len = 28)
plot_fct(allsites, groups, c(140, 150, 160, 180, 190, 200), mov_avg_len = 28)

# plot without confidence interval
plot_fct(allsites, groups, 20, stderr = FALSE, mov_avg_len = 28)
plot_fct(allsites, groups, c(50, 70, 80), stderr = FALSE, mov_avg_len = 28)
plot_fct(allsites, groups, c(140, 150, 160, 180, 190, 200), stderr = FALSE, mov_avg_len = 28)


## Buche 1-4, Eiche

# construct new groups
buei3sites_ind <- c()
buei3sites <- c(bu1, bu2, bu3, bu4, ei)
for (item in c(bu1_ind, bu2_ind, bu3_ind, bu4_ind, ei_ind)){
  buei3sites_ind[item] <- allsites[item]
}

# plot with confidence interval
plot_fct(buei3sites_ind, buei3sites, 20, filetitle = "Buche1234_Eiche", mov_avg_len = 28)
plot_fct(buei3sites_ind, buei3sites, c(50, 70, 80), filetitle = "Buche1234_Eiche", mov_avg_len = 28)
plot_fct(buei3sites_ind, buei3sites, c(140, 150, 160, 180, 190, 200), filetitle = "Buche1234_Eiche", mov_avg_len = 28)

# plot without confidence interval
plot_fct(buei3sites_ind, buei3sites, 20, filetitle = "Buche1234_Eiche", stderr = FALSE, mov_avg_len = 28)
plot_fct(buei3sites_ind, buei3sites, c(50, 70, 80), filetitle = "Buche1234_Eiche", stderr = FALSE, mov_avg_len = 28)
plot_fct(buei3sites_ind, buei3sites, c(140, 150, 160, 180, 190, 200), filetitle = "Buche1234_Eiche", stderr = FALSE, mov_avg_len = 28)
