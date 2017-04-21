from sklearn import model_selection # cross_val_score
from sklearn.metrics import precision_score, precision_recall_fscore_support, confusion_matrix
import numpy as np
import itertools
import matplotlib.pyplot as plt

# MORE INFO: http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
# Training data: X = n_samples x m_features
# NOTE

""" Plot confusion matrix: ref http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py"""
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def validation(classifier, data, y_data, y_target, class_names):
    #kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
    #cv = kfold
    x =  np.transpose(data)
    accuracy = model_selection.cross_val_score(classifier, x, y_target, scoring='accuracy')
    #precision = model_selection.cross_val_score(self.classifier, x, target, scoring='precision')
    #precision_score(y_true, y_pred, average='macro')  
    #recall = model_selection.cross_val_score(self.classifier, x, target, scoring='recall')
    precision, recall, fscore, m = precision_recall_fscore_support(y_target, y_data, average='macro')
    cnf_matrix = confusion_matrix(y_target, y_data)

    print("MLP Validation:")
    print(str(accuracy[0]) +", " +str(precision) +", " +str(recall))

    np.set_printoptions(precision=2)
    # Plot non-normalized confusion matrix
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=class_names, normalize = True, title='Confusion matrix')
    print ("... finishing matrix plot")
    plt.show()


def print_totals(y_predicted, y_target):
    p_totals = Counter(i for i in list(itertools.chain.from_iterable(y_predicted)))
    t_totals = Counter(i for i in list(itertools.chain.from_iterable(y_target)))

    print("\nPredicted #:")
    print(p_totals)
    print("\nTarget #:")
    print(t_totals)



    
            
       