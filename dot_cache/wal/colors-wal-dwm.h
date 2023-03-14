static const char norm_fg[] = "#dac0a6";
static const char norm_bg[] = "#0c0903";
static const char norm_border[] = "#988674";

static const char sel_fg[] = "#dac0a6";
static const char sel_bg[] = "#973720";
static const char sel_border[] = "#dac0a6";

static const char urg_fg[] = "#dac0a6";
static const char urg_bg[] = "#72482C";
static const char urg_border[] = "#72482C";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
