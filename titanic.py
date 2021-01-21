{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7103825136612022"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "# create df\n",
    "train = pd.read_csv('C:\\\\Shalin\\\\Springboard bootcamp\\\\Springboard repo_github\\\\Springboard-DS-Track\\\\Deploy model\\\\titanic.txt') # change file path\n",
    "# drop null values\n",
    "train.dropna(inplace=True)\n",
    "# features and target\n",
    "target = 'Survived'\n",
    "features = ['Pclass', 'Age', 'SibSp', 'Fare']\n",
    "# X matrix, y vector\n",
    "X = train[features]\n",
    "y = train[target]\n",
    "# model \n",
    "model = LogisticRegression()\n",
    "model.fit(X, y)\n",
    "model.score(X, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['model.pkl']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import joblib\n",
    "\n",
    "joblib.dump(model, \"model.pkl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "pickle.dump(model, open(\"model.pkl\", \"wb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
