const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0c0903", /* black   */
  [1] = "#72482C", /* red     */
  [2] = "#973720", /* green   */
  [3] = "#925736", /* yellow  */
  [4] = "#996647", /* blue    */
  [5] = "#97684C", /* magenta */
  [6] = "#AD7451", /* cyan    */
  [7] = "#dac0a6", /* white   */

  /* 8 bright colors */
  [8]  = "#988674",  /* black   */
  [9]  = "#72482C",  /* red     */
  [10] = "#973720", /* green   */
  [11] = "#925736", /* yellow  */
  [12] = "#996647", /* blue    */
  [13] = "#97684C", /* magenta */
  [14] = "#AD7451", /* cyan    */
  [15] = "#dac0a6", /* white   */

  /* special colors */
  [256] = "#0c0903", /* background */
  [257] = "#dac0a6", /* foreground */
  [258] = "#dac0a6",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
