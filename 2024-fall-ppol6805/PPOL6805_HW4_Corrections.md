**PPOL 6805 HW4 Corrections:**

* **Q1.2** Public Test: On the last line, please change `clust_` to `clust_i`
* **Q1.3** Public Test: Please add `num_trials <- 50` as the first line (before the lines calling `assert_that()`)
* **Q2.2**: When you call the `moran.plot()` function, please make sure to include `labels=clust_grid_sf$cell_name` as one of the arguments---this will just make sure that the points in the plot of the local Moran's $I$ values will be labeled with the name of the cell (so that you can "cross-check" the points with high local Moran's $I$ values in the plot with the actual grid points on the earlier $15 \times 15$ grid.
* **Q3.3** Public Test: Please remove any references to `us_sf` (this is from an earlier version of the homework, mentioned in the note above the main text for this problem!).
* **Q3.3** Public Test: Also please change any references to `dc_sf` to `dc_sfc`. (This change to the variable name was just to emphasize how the `spatstat` library requires `sfc` objects rather than full `sf` objects)
