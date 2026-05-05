__all__ = ['ols', 'lowess', 'rolling', 'ewm', 'expanding']

def ols(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Ordinary Least Squares (OLS) trendline function

    Requires `statsmodels` to be installed.

    This trendline function causes fit results to be stored within the figure,
    accessible via the `plotly.express.get_trendline_results` function. The fit results
    are the output of the `statsmodels.api.OLS` function.

    Valid keys for the `trendline_options` dict are:

    - `add_constant` (`bool`, default `True`): if `False`, the trendline passes through
    the origin but if `True` a y-intercept is fitted.

    - `log_x` and `log_y` (`bool`, default `False`): if `True` the OLS is computed with
    respect to the base 10 logarithm of the input. Note that this means no zeros can
    be present in the input.
    """
def lowess(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """LOcally WEighted Scatterplot Smoothing (LOWESS) trendline function

    Requires `statsmodels` to be installed.

    Valid keys for the `trendline_options` dict are:

    - `frac` (`float`, default `0.6666666`): the `frac` parameter from the
    `statsmodels.api.nonparametric.lowess` function
    """
def rolling(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Rolling trendline function

    The value of the `function` key of the `trendline_options` dict is the function to
    use (defaults to `mean`) and the value of the `function_args` key are taken to be
    its arguments as a dict. The remainder of  the `trendline_options` dict is passed as
    keyword arguments into the `pandas.Series.rolling` function.
    """
def expanding(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Expanding trendline function

    The value of the `function` key of the `trendline_options` dict is the function to
    use (defaults to `mean`) and the value of the `function_args` key are taken to be
    its arguments as a dict. The remainder of  the `trendline_options` dict is passed as
    keyword arguments into the `pandas.Series.expanding` function.
    """
def ewm(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Exponentially Weighted Moment (EWM) trendline function

    The value of the `function` key of the `trendline_options` dict is the function to
    use (defaults to `mean`) and the value of the `function_args` key are taken to be
    its arguments as a dict. The remainder of  the `trendline_options` dict is passed as
    keyword arguments into the `pandas.Series.ewm` function.
    """
