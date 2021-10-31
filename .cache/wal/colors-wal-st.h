const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#1f1118", /* black   */
  [1] = "#b35951", /* red     */
  [2] = "#6379a0", /* green   */
  [3] = "#6e88c3", /* yellow  */
  [4] = "#be7785", /* blue    */
  [5] = "#a5819f", /* magenta */
  [6] = "#e57476", /* cyan    */
  [7] = "#c7c3c5", /* white   */

  /* 8 bright colors */
  [8]  = "#574c51",  /* black   */
  [9]  = "#b35951",  /* red     */
  [10] = "#6379a0", /* green   */
  [11] = "#6e88c3", /* yellow  */
  [12] = "#be7785", /* blue    */
  [13] = "#a5819f", /* magenta */
  [14] = "#e57476", /* cyan    */
  [15] = "#c7c3c5", /* white   */

  /* special colors */
  [256] = "#1f1118", /* background */
  [257] = "#c7c3c5", /* foreground */
  [258] = "#c7c3c5",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
