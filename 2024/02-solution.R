##################################################
## load required libraries #######################
##################################################

library(purrr) ## functional programming or die trying

##################################################
## read in data ##################################
##################################################

## read in data as a list, since sequences have variable lengths
data <- "02-input.txt" |>
  readLines() |>
  strsplit(' ') |>
  map(as.integer)
                  
##################################################
## define functions ##############################
##################################################

check_for_violations <- function(x){
  diffs <- diff(x)
  return(all(abs(diffs) <= 3) & (all(diffs < 0) | all(diffs > 0)))
}

##################################################
## check for violations: part A ##################
##################################################

data |>
  map_lgl(check_for_violations) |>
  sum()

##################################################
## check for violations: part B ##################
##################################################

data |>
  map_lgl(function(x) {
    if (check_for_violations(x)) return(TRUE)
    
    for(i in seq_along(x)) {
      if (check_for_violations(x[-i])) return(TRUE)
    }
    return(FALSE)
  }) |> 
  sum()

##################################################
## references ####################################
##################################################

## Stack Overflow: read.table examples
## https://stackoverflow.com/questions/18922493/how-can-you-read-a-csv-file-in-r-with-different-number-of-columns

## Data Science Learning Community Slack convos, purrr examples
## including from Gus Lipkin, Emil Hvitfeldt