set.seed(5300)
library(tidyverse) |> suppressPackageStartupMessages()

# For order randomization:

randomize_order <- function(items) {
  return(sample(items))
}
add_blanks <- function(items, prefix="* ___ ") {
  return(paste0(prefix,items))
}
join_lines <- function(lines) {
  return(paste(lines, collapse='\n'))
}
randomized_output <- function(items, prefix="* ___ ") {
  randomized_items <- randomize_order(items)
  random_with_blanks <- add_blanks(randomized_items, prefix)
  random_joined <- join_lines(random_with_blanks)
  return(random_joined)
}

# Example usage in .qmd file:
# #| label: q1-options
# #| output: asis
# q1_items <- c(
#   "Client (laptop) sends a request (typically GET or POST) to URL to request HTML/CSS/JS code from host (server)",
#   "Host transmits HTML/CSS/JS code over the internet (using HTTP(S)) to the client's RAM",
#   "Specialized rendering software (browser) interprets the HTML commands as graphical instructions",
#   "Webpage shows up on client's screen"
# )
# q1_md <- randomized_output(q1_items)
# writeLines(q1_md)

# For matching questions:

pad_uneven_cols <- function(x, y) {
  longest <- max(length(x), length(y))
  x_gap <- longest - length(x)
  x_pad <- rep("", x_gap)
  y_gap <- longest - length(y)
  y_pad <- rep("", y_gap)
  return(list(
    c(x, x_pad),
    c(y, y_pad)
  ))
}
random_match_output <- function(left_items, right_items, headers=c("",""), mid_spacer=TRUE) {
  # Construct left column
  left_order <- randomize_order(left_items)
  left_blanks <- add_blanks(left_order, prefix="___ ")
  right_order <- randomize_order(right_items)
  right_ids <- paste0("**(", letters[1:length(right_order)], ")**")
  right_vals <- paste0(right_ids, " ", right_order)
  padded_cols <- pad_uneven_cols(left_blanks, right_vals)
  left_pad <- padded_cols[[1]]
  right_pad <- padded_cols[[2]]
  rand_cols_df <- tibble(
    left=left_pad,
    right=right_pad
  )
  rand_col_names <- headers
  if (mid_spacer) {
    rand_cols_df <- rand_cols_df |>
      mutate(mid=" ") |>
      select(left, mid, right)
    rand_col_names <- c(headers[1], "", headers[2])
  }
  names(rand_cols_df) <- rand_col_names
  return(rand_cols_df)
}

# Example usage in .qmd file:
# headers <- c("Goal", "Quarto CLI Command")
# q4_left <- c(
#   "Producing desired output document(s) from input `.qmd` file(s)",
#   "Changing a `.qmd` or `.ipynb` file to a different notebook format",
#   "Viewing a Quarto document in a live, interactive mode, optimized for quickly checking the results of changes to the input document (and *not* optimized for completeness---for example, not optimized for having an up-to-date navbar)"
# )
# q4_right <- c(
#   "`quarto render`",
#   "`quarto convert`",
#   "`quarto preview`"
# )
# random_match_output(q4_left, q4_right, headers, mid_spacer=FALSE)
