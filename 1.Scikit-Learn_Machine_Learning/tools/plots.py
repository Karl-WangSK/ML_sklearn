from .plot_2d_separator import plot_2d_classification, plot_2d_separator
from .plot_helpers import cm2, cm3
from .plot_agglomerative import plot_agglomerative, plot_agglomerative_algorithm
from .plot_improper_preprocessing import plot_improper_processing, plot_proper_processing
from .plot_cross_validation import (plot_threefold_split, plot_label_kfold,
                                    plot_shuffle_split, plot_cross_validation,
                                    plot_stratified_cross_validation)

from .plot_grid_search import plot_grid_search_overview, plot_cross_val_selection
from .plot_metrics import (plot_confusion_matrix_illustration,
                           plot_binary_confusion_matrix,
                           plot_decision_threshold)

__all__ = ['plot_2d_classification',
           'plot_2d_separator',
           'cm3', 'cm2', 'plot_improper_processing', 'plot_proper_processing',
           'plot_label_kfold',
           'plot_shuffle_split',
           'plot_stratified_cross_validation',
           'plot_threefold_split',
           'plot_cross_validation',
           'plot_grid_search_overview',
           'plot_cross_val_selection',
           'plot_confusion_matrix_illustration',
           'plot_binary_confusion_matrix',
           'plot_decision_threshold'
           ]
