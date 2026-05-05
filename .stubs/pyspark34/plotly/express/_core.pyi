from ._special_inputs import Constant as Constant, IdentityMap as IdentityMap, Range as Range
from .trendline_functions import ewm as ewm, expanding as expanding, lowess as lowess, ols as ols, rolling as rolling
from _typeshed import Incomplete
from plotly._subplots import make_subplots as make_subplots
from plotly.colors import qualitative as qualitative, sequential as sequential
from typing import NamedTuple

NO_COLOR: str
trendline_functions: Incomplete
direct_attrables: Incomplete
array_attrables: Incomplete
group_attrables: Incomplete
renameable_group_attrables: Incomplete
all_attrables: Incomplete
cartesians: Incomplete

class PxDefaults:
    def __init__(self) -> None: ...
    template: Incomplete
    width: Incomplete
    height: Incomplete
    color_discrete_sequence: Incomplete
    color_discrete_map: Incomplete
    color_continuous_scale: Incomplete
    symbol_sequence: Incomplete
    symbol_map: Incomplete
    line_dash_sequence: Incomplete
    line_dash_map: Incomplete
    pattern_shape_sequence: Incomplete
    pattern_shape_map: Incomplete
    size_max: int
    category_orders: Incomplete
    labels: Incomplete
    def reset(self) -> None: ...

defaults: Incomplete
MAPBOX_TOKEN: Incomplete

def set_mapbox_access_token(token) -> None:
    """
    Arguments:
        token: A Mapbox token to be used in `plotly.express.scatter_mapbox` and         `plotly.express.line_mapbox` figures. See         https://docs.mapbox.com/help/how-mapbox-works/access-tokens/ for more details
    """
def get_trendline_results(fig):
    '''
    Extracts fit statistics for trendlines (when applied to figures generated with
    the `trendline` argument set to `"ols"`).

    Arguments:
        fig: the output of a `plotly.express` charting call
    Returns:
        A `pandas.DataFrame` with a column "px_fit_results" containing the `statsmodels`
        results objects, along with columns identifying the subset of the data the
        trendline was fit on.
    '''

class Mapping(NamedTuple):
    show_in_trace_name: Incomplete
    grouper: Incomplete
    val_map: Incomplete
    sequence: Incomplete
    updater: Incomplete
    variable: Incomplete
    facet: Incomplete

class TraceSpec(NamedTuple):
    constructor: Incomplete
    attrs: Incomplete
    trace_patch: Incomplete
    marginal: Incomplete

def get_label(args, column): ...
def invert_label(args, column):
    '''Invert mapping.
    Find key corresponding to value column in dict args["labels"].
    Returns `column` if the value does not exist.
    '''
def get_decorated_label(args, column, role): ...
def make_mapping(args, variable): ...
def make_trace_kwargs(args, trace_spec, trace_data, mapping_labels, sizeref):
    """Populates a dict with arguments to update trace

    Parameters
    ----------
    args : dict
        args to be used for the trace
    trace_spec : NamedTuple
        which kind of trace to be used (has constructor, marginal etc.
        attributes)
    trace_data : pandas DataFrame
        data
    mapping_labels : dict
        to be used for hovertemplate
    sizeref : float
        marker sizeref

    Returns
    -------
    trace_patch : dict
        dict to be used to update trace
    fit_results : dict
        fit information to be used for trendlines
    """
def configure_axes(args, constructor, fig, orders) -> None: ...
def set_cartesian_axis_opts(args, axis, letter, orders) -> None: ...
def configure_cartesian_marginal_axes(args, fig, orders) -> None: ...
def configure_cartesian_axes(args, fig, orders) -> None: ...
def configure_ternary_axes(args, fig, orders) -> None: ...
def configure_polar_axes(args, fig, orders) -> None: ...
def configure_3d_axes(args, fig, orders) -> None: ...
def configure_mapbox(args, fig, orders) -> None: ...
def configure_geo(args, fig, orders) -> None: ...
def configure_animation_controls(args, constructor, fig): ...
def make_trace_spec(args, constructor, attrs, trace_patch): ...
def make_trendline_spec(args, constructor): ...
def one_group(x): ...
def apply_default_cascade(args) -> None: ...
def to_unindexed_series(x, name: Incomplete | None = None):
    """
    assuming x is list-like or even an existing pd.Series, return a new pd.Series with
    no index, without extracting the data from an existing Series via numpy, which
    seems to mangle datetime columns. Stripping the index from existing pd.Series is
    required to get things to match up right in the new DataFrame we're building
    """
def process_args_into_dataframe(args, wide_mode, var_name, value_name):
    '''
    After this function runs, the `all_attrables` keys of `args` all contain only
    references to columns of `df_output`. This function handles the extraction of data
    from `args["attrable"]` and column-name-generation as appropriate, and adds the
    data to `df_output` and then replaces `args["attrable"]` with the appropriate
    reference.
    '''
def build_dataframe(args, constructor):
    """
    Constructs a dataframe and modifies `args` in-place.

    The argument values in `args` can be either strings corresponding to
    existing columns of a dataframe, or data arrays (lists, numpy arrays,
    pandas columns, series).

    Parameters
    ----------
    args : OrderedDict
        arguments passed to the px function and subsequently modified
    constructor : graph_object trace class
        the trace type selected for this figure
    """
def process_dataframe_hierarchy(args):
    """
    Build dataframe for sunburst, treemap, or icicle when the path argument is provided.
    """
def process_dataframe_timeline(args):
    """
    Massage input for bar traces for px.timeline()
    """
def process_dataframe_pie(args, trace_patch): ...
def infer_config(args, constructor, trace_patch, layout_patch): ...
def get_groups_and_orders(args, grouper):
    '''
    `orders` is the user-supplied ordering with the remaining data-frame-supplied
    ordering appended if the column is used for grouping. It includes anything the user
    gave, for any variable, including values not present in the dataset. It\'s a dict
    where the keys are e.g. "x" or "color"

    `groups` is the dicts of groups, ordered by the order above. Its keys are
    tuples like [("value1", ""), ("value2", "")] where each tuple contains the name
    of a single dimension-group
    '''
def make_figure(args, constructor, trace_patch: Incomplete | None = None, layout_patch: Incomplete | None = None): ...
def init_figure(args, subplot_type, frame_list, nrows, ncols, col_labels, row_labels): ...
