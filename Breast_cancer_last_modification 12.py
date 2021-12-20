{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Reading the file with pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>1000025</th>\n",
       "      <th>5</th>\n",
       "      <th>1</th>\n",
       "      <th>1.1</th>\n",
       "      <th>1.2</th>\n",
       "      <th>2</th>\n",
       "      <th>1.3</th>\n",
       "      <th>3</th>\n",
       "      <th>1.4</th>\n",
       "      <th>1.5</th>\n",
       "      <th>2.1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1002945</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>7</td>\n",
       "      <td>10</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1015425</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1016277</td>\n",
       "      <td>6</td>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1017023</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1017122</td>\n",
       "      <td>8</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>10</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   1000025  5   1  1.1  1.2  2 1.3  3  1.4  1.5  2.1\n",
       "0  1002945  5   4    4    5  7  10  3    2    1    2\n",
       "1  1015425  3   1    1    1  2   2  3    1    1    2\n",
       "2  1016277  6   8    8    1  3   4  3    7    1    2\n",
       "3  1017023  4   1    1    3  2   1  3    1    1    2\n",
       "4  1017122  8  10   10    8  7  10  9    7    1    4"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data=pd.read_csv(\"breast-cancer-wisconsin.data\")\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Give the name of the columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sample code number</th>\n",
       "      <th>Clump Thickness</th>\n",
       "      <th>Uniformity of Cell Size</th>\n",
       "      <th>Uniformity of Cell Shape</th>\n",
       "      <th>Marginal Adhesion</th>\n",
       "      <th>Single Epithelial Cell Size</th>\n",
       "      <th>Bare Nuclei</th>\n",
       "      <th>Bland Chromatin</th>\n",
       "      <th>Normal Nucleoli</th>\n",
       "      <th>Mitoses</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000025</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1002945</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>7</td>\n",
       "      <td>10</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1015425</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1016277</td>\n",
       "      <td>6</td>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1017023</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sample code number  Clump Thickness  Uniformity of Cell Size  \\\n",
       "0             1000025                5                        1   \n",
       "1             1002945                5                        4   \n",
       "2             1015425                3                        1   \n",
       "3             1016277                6                        8   \n",
       "4             1017023                4                        1   \n",
       "\n",
       "   Uniformity of Cell Shape  Marginal Adhesion  Single Epithelial Cell Size  \\\n",
       "0                         1                  1                            2   \n",
       "1                         4                  5                            7   \n",
       "2                         1                  1                            2   \n",
       "3                         8                  1                            3   \n",
       "4                         1                  3                            2   \n",
       "\n",
       "  Bare Nuclei  Bland Chromatin  Normal Nucleoli  Mitoses  Class  \n",
       "0           1                3                1        1      2  \n",
       "1          10                3                2        1      2  \n",
       "2           2                3                1        1      2  \n",
       "3           4                3                7        1      2  \n",
       "4           1                3                1        1      2  "
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data=pd.read_csv(\"breast-cancer-wisconsin.data\",names=[\n",
    "     \"Sample code number\",\n",
    "    \"Clump Thickness\",\n",
    "     \"Uniformity of Cell Size\",\n",
    "     \"Uniformity of Cell Shape\",\n",
    "     \"Marginal Adhesion\",\n",
    "     \"Single Epithelial Cell Size\",\n",
    "     \"Bare Nuclei\",\n",
    "     \"Bland Chromatin\",\n",
    "     \"Normal Nucleoli\",\n",
    "     \"Mitoses\",\n",
    "     \"Class\"])\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Data type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sample code number              int64\n",
       "Clump Thickness                 int64\n",
       "Uniformity of Cell Size         int64\n",
       "Uniformity of Cell Shape        int64\n",
       "Marginal Adhesion               int64\n",
       "Single Epithelial Cell Size     int64\n",
       "Bare Nuclei                    object\n",
       "Bland Chromatin                 int64\n",
       "Normal Nucleoli                 int64\n",
       "Mitoses                         int64\n",
       "Class                           int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Defining non nummeric Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Is_non_numeric(x):\n",
    "    return not x.isnumeric()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "mask=data['Bare Nuclei'].apply(Is_non_numeric)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sample code number</th>\n",
       "      <th>Clump Thickness</th>\n",
       "      <th>Uniformity of Cell Size</th>\n",
       "      <th>Uniformity of Cell Shape</th>\n",
       "      <th>Marginal Adhesion</th>\n",
       "      <th>Single Epithelial Cell Size</th>\n",
       "      <th>Bare Nuclei</th>\n",
       "      <th>Bland Chromatin</th>\n",
       "      <th>Normal Nucleoli</th>\n",
       "      <th>Mitoses</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>1057013</td>\n",
       "      <td>8</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>?</td>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>1096800</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>6</td>\n",
       "      <td>?</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>139</th>\n",
       "      <td>1183246</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>?</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>1184840</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>?</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>158</th>\n",
       "      <td>1193683</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>?</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Sample code number  Clump Thickness  Uniformity of Cell Size  \\\n",
       "23              1057013                8                        4   \n",
       "40              1096800                6                        6   \n",
       "139             1183246                1                        1   \n",
       "145             1184840                1                        1   \n",
       "158             1193683                1                        1   \n",
       "\n",
       "     Uniformity of Cell Shape  Marginal Adhesion  Single Epithelial Cell Size  \\\n",
       "23                          5                  1                            2   \n",
       "40                          6                  9                            6   \n",
       "139                         1                  1                            1   \n",
       "145                         3                  1                            2   \n",
       "158                         2                  1                            3   \n",
       "\n",
       "    Bare Nuclei  Bland Chromatin  Normal Nucleoli  Mitoses  Class  \n",
       "23            ?                7                3        1      4  \n",
       "40            ?                7                8        1      2  \n",
       "139           ?                2                1        1      2  \n",
       "145           ?                2                1        1      2  \n",
       "158           ?                1                1        1      2  "
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_non_numeric=data[mask]\n",
    "data_non_numeric.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display numeric data only:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sample code number</th>\n",
       "      <th>Clump Thickness</th>\n",
       "      <th>Uniformity of Cell Size</th>\n",
       "      <th>Uniformity of Cell Shape</th>\n",
       "      <th>Marginal Adhesion</th>\n",
       "      <th>Single Epithelial Cell Size</th>\n",
       "      <th>Bare Nuclei</th>\n",
       "      <th>Bland Chromatin</th>\n",
       "      <th>Normal Nucleoli</th>\n",
       "      <th>Mitoses</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000025</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1002945</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>7</td>\n",
       "      <td>10</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1015425</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1016277</td>\n",
       "      <td>6</td>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1017023</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sample code number  Clump Thickness  Uniformity of Cell Size  \\\n",
       "0             1000025                5                        1   \n",
       "1             1002945                5                        4   \n",
       "2             1015425                3                        1   \n",
       "3             1016277                6                        8   \n",
       "4             1017023                4                        1   \n",
       "\n",
       "   Uniformity of Cell Shape  Marginal Adhesion  Single Epithelial Cell Size  \\\n",
       "0                         1                  1                            2   \n",
       "1                         4                  5                            7   \n",
       "2                         1                  1                            2   \n",
       "3                         8                  1                            3   \n",
       "4                         1                  3                            2   \n",
       "\n",
       "  Bare Nuclei  Bland Chromatin  Normal Nucleoli  Mitoses  Class  \n",
       "0           1                3                1        1      2  \n",
       "1          10                3                2        1      2  \n",
       "2           2                3                1        1      2  \n",
       "3           4                3                7        1      2  \n",
       "4           1                3                1        1      2  "
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_numeric=(data[~mask])\n",
    "data_numeric.head()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Defining input features:\n",
    "    Delete Sample code Number (Id)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_input=data_numeric.drop(columns=['Sample code number','Class'])\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Defining output:\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_output=data_numeric['Class']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "change the values   to  0 or 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_output=data_output.replace({2:0,4:1})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    0\n",
       "1    0\n",
       "2    0\n",
       "3    0\n",
       "4    0\n",
       "Name: Class, dtype: int64"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_output.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "x,x_test,y,y_test=train_test_split(data_input,data_output,test_size=.33,random_state=2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Insert the remaining data to 33% for validation and 67% for training"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_val,y_train,y_val=train_test_split(x,y,test_size=0.33,random_state=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(226, 9)\n",
      "(226,)\n"
     ]
    }
   ],
   "source": [
    "print(x_test.shape)\n",
    "print(y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "model=DecisionTreeClassifier(max_depth=3,random_state=2)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Training:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(ccp_alpha=0.0, class_weight=None, criterion='gini',\n",
       "                       max_depth=3, max_features=None, max_leaf_nodes=None,\n",
       "                       min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "                       min_samples_leaf=1, min_samples_split=2,\n",
       "                       min_weight_fraction_leaf=0.0, presort='deprecated',\n",
       "                       random_state=2, splitter='best')"
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Validation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred_train=model.predict(x_train)\n",
    "y_pred_val=model.predict(x_val)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here we will measure the accuracy:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9803921568627451\n",
      "0.9668874172185431\n"
     ]
    }
   ],
   "source": [
    "print(accuracy_score(y_train,y_pred_train))\n",
    "print(accuracy_score(y_val,y_pred_val))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "for loop to test many values of max_depth :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [],
   "source": [
    "max_depth_values=[1,2,3,4,5,6,7,8]\n",
    "train_accuracy_values=[]\n",
    "val_accuracy_values=[]\n",
    "for max_depth_val in  max_depth_values:\n",
    "    model=DecisionTreeClassifier(max_depth=max_depth_val,random_state=2)\n",
    "    model.fit(x_train,y_train)\n",
    "    y_pred_train=model.predict(x_train)\n",
    "    y_pred_val=model.predict(x_val)\n",
    "    acc_train=accuracy_score(y_train,y_pred_train)\n",
    "    acc_val=accuracy_score(y_val,y_pred_val)\n",
    "    train_accuracy_values.append(acc_train)\n",
    "    val_accuracy_values.append(acc_val)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Graph for the values:\n",
    "3 is the best value for max_depth"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEXCAYAAAC3c9OwAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nO3dd3xUZdr/8c9FCAmQEEogdAJK6EgXRVmwLYoVWMWCuruCBdu6btHHn9j20X0WEOwFWXUtqIAdpRkUUKQv1YQqhBI6JIRAyvX745zgECfJhGRyZpLr/XrNi5k5Zb6ZkLnm3Pd97iOqijHGGFNYNa8DGGOMCU1WIIwxxvhlBcIYY4xfViCMMcb4ZQXCGGOMX1YgjDHG+GUFwpRIHP8WkYMisth97k4RSReRTBFp4GG2kMhREhF5U0SeCtK+HxORd4Kxb1O1WYEwgTgPuBhorqp9RCQSGA9coqoxqrr/dHYqIokioiJS/TS3L5cc4UREBohImtc5TNVgBcIEohWwVVWPuo8TgGhgrXeRQiqHKQX3iNQ+e8KA/ZIMACLSVESmicheEdkiIve6z/8RmASc4zbjvA+kuJsdEpFv3PXai8hsETkgIikicq3PvmuKyDgR+VlEDovIAhGpCXzns59METnHT64oEZkgIjvd2wT3uSR/OQptW3CE8nsR2e42kd0hIr1FZJWIHBKRF3zWP0NEvhGR/SKyT0TeFZG6PssOiEgPn/drn4gMKOL97C4iy0UkQ0Q+wClkvssvF5GVbobvRaSrz7KtIvKQiKxzM/9bRKJFpDbwFdDUfb8yRaSpu1kNEXnbfb21ItLLXy53/xPd9+OIiCwTkfN9lkWIyMMissnd1zIRaeHvaE9E5onIbe79U5q5Cq/vrvsPEVkIZAFt3N/Levd1NovI7YVyXuW+R0fcPINE5HcisqzQen8WkU+K+nlNGaiq3ar4DeeLwjLgUaAG0AbYDPzWXX4rsMBn/URAgeru49rAduD3QHWgB7AP6OQufxGYBzQDIoBzgajC+yki2xPAIqAR0BD4HnjSXw4/2xYsfwXnA/oSIBv4xN1fM2AP8Bt3/TNxmtKi3Nf6Dpjgs7+RwHqgFjATGFvE69YAfgb+BEQCw4Ac4Cl3eQ/3dc92349bgK1AlLt8K7AGaAHUBxb6bDsASCv0eo+5P9dl7v6eBhYV857eBDRwf1d/BnYD0e6yvwCrgXaAAGe56/7qvXZ/p7f5ZHinmP8j84BtQCf3dSOBwcAZ7uv8Bqdw9HDX7wMcdn8f1dzfVXv3d3MA6ODzWiuAoV7/HVXGm+cB7Ob9zf2g2lbouYeAf7v3b6X4AnEdML/Q9q8CY9w/7mPAWX5e91cfOn7W2QRc5vP4tzjNXSVu77O8mc9z+4HrfB5PA+4vYvurgRWFnvvM/QBdhfuB7me7/sBOQHye+55fPuRfxi1yPstT+KVQbQXu8Fl2GbDJvT8A/wVijs/jjsCxUvz+Dxb8ftwcVwXyu6L0BeKJEnJ8Atzn8//n2SLWexn4h3u/k5vf7+/CbmW7WROTAaePoanb3HFIRA4BD+O08Qe6/dmFtr8RaAzE43x733Sa2ZrifBsv8LP7XGmk+9w/5udxDICINBKRKSKyQ0SOAO/g5Pf1OtAZeF5VjxeTeYe6n2A+uQu0Av5c6P1qUejn2l5o25J+5t0+97OAaCmi899tklnvNvcdAuL45edswen/rkri+zMhIpeKyCK36e4QTiEMJMdbwA0iIsAI4MNifhemDKxAGHD+cLeoal2fW6yqXlaK7b8ttH2Mqt6J09SUjdOUUFggUwnvxPlALdDSfS4YnsbJ1FVV6+A0xUjBQhGJASYAbwCPiUj9IvazC2jmfoAVaOlzfzvON2Df96uWqr7vs06LQtsW/Mxlmn7Z7W/4G3AtUE9V6+I05RRk3Y7/31XBAIVaPs81LrS8qGUFTmYXkSico7exQIKbY0YAOVDVRcAJ4HzgBuA//tYzZWcFwgAsBo6IyN/E6VCOEJHOItI7wO2/AJJEZISIRLq33iLSQVXzgcnAeLdjN0JEznE/IPYC+Th9HkV5H3hERBqKSDxOP0mwxvzHApk4nd7NcNrjfU0ElqnqbcCXOH0b/vwA5AL3ikh1ERmC06Ze4HXgDhE5Wxy1RWSwiMT6rDNaRJq7Rehh4AP3+XSggYjEleFnzMV576uLyKNAHZ/lk4AnRaStm62riDRQ1b3ADuAm93f4B079AF8J9BeRlm62h0rIUQOnP2EvkCsil+L0ERV4A/i9iFwoItVEpJmItPdZ/jbwApCrqgtK+yaYwFiBMKhqHnAF0A3YgvOtfxJO00Mg22fg/HEPx/mmuxv4J84HAMCDOO32S3A6GP8JVFPVLOAfwEK3qaWvn90/BSzFafNfDSx3nwuGx3E6kA/jFIDpBQtE5CpgEHCH+9QDQA8RubHwTlT1BDAEp+/mIE4fzXSf5UtxOrxfcJdvdNf19R4wC2ewwGbcn1lVf8Ipmpvd96y0zW0zcUZCpeI0XWVzatPPeOBD97WP4HxQ13SXjcQpmvtx2v6/9/mZZuMUsVU4Ax6+KC6E+3/mXve1DuIcCXzms3wxzqCHZ3F+H99y6pHkf3Ca+uzoIYjk1GZSY4zXRGQrTufvHK+zhCpxhknvwRn1tMHrPJWVHUEYY8LRncASKw7BdVpTHBhjjFfcIyzBGYZsgsiamIwxxvhlTUzGGGP8qjRNTPHx8ZqYmHja2x89epTatWuXX6AgCqesEF55wykrhFfecMoK4ZW3LFmXLVu2T1Ub+l3o9anc5XXr2bOnlkVycnKZtq9I4ZRVNbzyhlNW1fDKG05ZVcMrb1myAkvVptowxhhTGlYgjDHG+GUFwhhjjF+VppPan5ycHNLS0sjOzi5x3bi4ONavX18BqcquIrJGR0fTvHlzIiMjg/o6xpjQVakLRFpaGrGxsSQmJnLqxJq/lpGRQWxsbLHrhIpgZ1VV9u/fT1paGq1btw7a6xhjQlvQmphEZLKI7BGRNUUsFxF5TkQ2inP5xx4+y24RkQ3u7ZbTzZCdnU2DBg1KLA7mVCJCgwYNAjryMsZUXsHsg3gTZ/bLolwKtHVvo3CuEoU7vfEYnKuc9QHGiEi90w1hxeH02PtmjAlagVDV73Cmdi7KVcDb7lDcRUBdEWmCc0nJ2ap6QFUPArMpvtAYY0yVk5uXz8Y9GXy5aheLd+cG5TW87INoxqnz0Ke5zxX1/K+IyCicow8SEhKYN2/eKcvj4uLIyMgIKExeXl7A63rpxRdf5Oabby71dk899RT9+vVj4MCBAW+TnZ39q/f0dGRmZpbLfipCOGWF8MobTlkhdPLmq7L/mLIjM5+0zHx2ZOSTlqnsyswn151Kr1ktpU8QsnpZIPy1YWgxz//6SdXXgNcAevXqpQMGDDhl+fr16wPuzA2XTupXXnmF4cOH+82al5dHRESE3+3++c9/lvq1oqOj6d69e6m3K2zevHkU/t2EqnDKCuGVN5yyQsXnVVX2ZZ4gNT2DlN0ZpKZn8NPuDDakZ3D0RN7J9ZrVrUlS0xguaxxL+8axJCXEsmP98qBk9bJApHHqdXeb41yNLA0YUOj5eRWWqpxdffXVbN++nezsbO677z5GjRoFwNdff83DDz9MXl4e8fHxzJ07l8zMTO655x6WLl2KiDBmzBiGDh16cl/PPfccO3fuZPDgwTRq1Ijk5GRiYmJ44IEHmDlzJuPGjeObb77h888/59ixY5x77rm8+uqriAi33norl19+OcOGDSMxMZFbbrmFzz//nJycHD766CPat29f1I9gjClnR7Jz2JCeQcruTFJ2HyElPYPU9EwOHD1xcp36tWvQLiGW3/VqQTu3ELRNiKFO9K+Hnu9NDU6foZcF4jPgbhGZgtMhfVhVd4nITOB/fTqmL6Hk69uW6PHP17Ju55Eilxf37bsoHZvWYcwVnYpdZ/LkydSvX59jx47Ru3dvhg4dSn5+PiNHjuS7776jdevWHDjgdNU8+eSTxMXFsXr1agAOHjx4yr7uvfdexo8fz5dffknBxIRHjx6lc+fOPPHEE06mjh159NFHARgxYgRffPEFV1xxxa9yxcfHs3z5cl566SXGjh3LpEmTSvWzG2NKlp2Tx8Y9mSePClLSM0jdncHOw7+MEKxdI4KkxrFc0jGBdo1jaZcQS1LjWOJjoorZc8UIWoEQkfdxjgTiRSQNZ2RSJICqvgLMAC7DuR5vFs71Z1HVAyLyJM71iwGeUNXiOrtD2nPPPcfHH38MwPbt29mwYQN79+6lf//+J88xqF+/PgBz5sxhypQpJ7etV6/kwVsRERGnHGUkJyfzf//3f2RlZXHgwAE6derkt0AMGTIEgJ49ezJ9+vRfLTfGBC43L5+t+7NONguluk1EW/cfJd9tIK8RUY0zGsXQp3V92jWuQ7vGMSQlxNKsbs2QHTUYtAKhqteXsFyB0UUsmwxMLs88JX3TD0YfxLx585gzZw4//PADtWrVYsCAAWRnZ6Oqfv9DFPV8caKjo08e+WRnZ3PXXXexdOlSWrRowWOPPVbkuQxRUc63k4iICHJzgzMCwpjKRlXZcejYKYUgJT2TTXsyOZGXD0A1gcQGtUlKiOWKs5qebB5KbFCL6hHhNbtRpT6T2muHDx+mXr161KpVi59++olFixYBcM455zB69Gi2bNlysompfv36XHLJJbzwwgtMmDABcJqYCh9FxMbGFjnaqqAYxMfHk5mZydSpUxk2bFgQf0JjKq8jx5XvN+5zCkG60zy0IT2TzOO/fKFqGhdNUuNY+ifFO01DCbGc2SiG6MjSNVeHKisQQTRo0CBeeeUVunbtSrt27ejbty8ADRs25LXXXmPIkCHk5+fTqFEjZs+ezSOPPMLo0aPp3LkzERERjBkz5mRTUIFRo0YxdOhQmjVrRnJy8inL6taty8iRI+nSpQuJiYn07t27wn5WYwrk5ytpB4/x0+4j7gdrJqm7M9h18Cg1Fsz2Ol5ATuTmcyQ7F5J/BKBerUjaNY5lWM/mJCXE0q5xDG0TYv12GFcmleaa1L169dKlS5ee8tz69evp0KFDQNuHyzBXqLispXn/ihNOwxvDKSt4m1dV2Ztx/Jdv2O6/qemZHMv5ZVhm83o1aZcQS97RAzRr2tSTrKUVUU3IPbiLwed1JykhlviYGiHbTwBl+38gIstUtZe/ZXYEYYwp0eGsHFL3+La7O8XgUFbOyXXiY6Jo1ziG6/u0PNkB2zYhlpgo52PG+RDr4tWPUGrz5u2j35nxXsfwlBUIY8xJx044wzILNw/tPvLLYIfYqOokNY7l0s5NTp6olZQQQ4MQGJZpypcVCGOqoJy8fLbuO0pKwfh8t3no5wNZFLQ616hejbaNYjj3jAbOSBx3jH6TuOiQbm4x5ccKhDGVWH6+Myyz4CStgkKwaW8mOXlOJYioJiQ2qEXHpnW4pnvzk81DrRrUJqKaFYKqzAqEMZWAqrI38zipuzPdQnCElPRMNqRnkFVoHp92jWMZ0K7RyeahNg1rV5phmaZ8WYEwJgwdO5HH56t2MnPdcV5O+YHU9AwOntJhXIOkhFiu7dXCKQSNY2nbKIbYSj4s05QvKxAhJiYmhszMzFOeO3ToEO+99x533XVXqfd32WWX8d5771G3bt3yimg8dDw3jymLt/NC8kb2ZhwnOgI6NstnUOfGJ+fwcYZlWoexKTsrEGHg0KFDvPTSS34LREmTDM6YMSOY0UwFyc3LZ/ryHUycu4Edh47Rp3V9Xri+O1k/r2LgwH5exzOVVHhNDBJm/va3v/HSSy+dfPzYY48xbtw4MjMzufDCC+nRowddunTh008/LXY/f//739m0aRPdunXjL3/5C/Pnz2fgwIHccMMNdOnijCu/+uqr6dmzJ506deK11147uW1iYiL79u1j69atdOjQgZEjR9KpUycuueQSjh07Fpwf3JSb/Hzl05U7uPjZ7/jrtFXEx0bxzh/P5oNRfTm7jV1v3QRX1TmC+OrvsHt1kYtr5uVCRCnfjsZd4NJnilw8fPhw7r///pPf/D/88EO+/vproqOj+fjjj6lTpw779u2jb9++XHnllUX+sT/zzDOsWbOGlStXAs5RweLFi1mzZs3JGWH9TSveoEGDU/azYcMG3n//fV5//XWuvfZapk2bxk033VS6n9lUCFVl1rp0xs9KJSU9g/aNY3n95l5c1KGRFQVTYapOgfBA9+7d2bNnDzt37mTv3r3Uq1ePli1bkpOTw8MPP8x3331HtWrV2LFjB+np6TRu3Djgfffp0+dkcQD/04oXLhCtW7emW7dugDPN99atW8v+Q5pypap8t2Ef42alsCrtMG0a1ub567szuEsTqtmQU1PBqk6BKOabPsCxIM1vNGzYMKZOncru3bsZPnw4AO+++y579+5l2bJlREZGkpiYWOS03EWpXbv2yftFTSteWMEU3+BM821NTKHlx837GTcrlcVbD9C8Xk3+Nawr13RvFnZTRJvKo+oUCI8MHz6ckSNHsm/fPr799lvAmQa8UaNGREZGkpyczM8//1zsPoqb4rtgf/6mFTfhYeX2Q4yblcL8DftIqBPFk1d35rpeLahR3QqD8ZYViCDr1KkTGRkZNGvWjCZNmgBw4403csUVV9CrVy+6detW4vWgGzRoQL9+/ejcuTOXXnopAwcOPGV5UdOKm9C2ftcRxs1KZc76dOrXrsEjgztwU99WdtKaCRlWICpAwTWmC8THx/PDDz/4XbfwORAF3nvvvZP3MzIyuOyyy04+joqK4quvvvK7XUE/Q3x8PGvWrDn5/IMPPhhQdlP+Nu3N5NnZqXyxahex0dV58JIkbu3X+uSsp8aECvsfaUwF2X4gi+fmbmDa8jSiIyO4e+CZjDy/DXG17OxmE5qsQBgTZOlHsnn+mw18sGQ7IsIf+rXmzgFn2PTYJuRV+gKhqjZu/DRUlisNeml/5nFe+XYTb//wM3n5yvA+Lbh7YFsax0V7Hc2YgFTqAhEdHc3+/ftp0MDOOC0NVWX//v1ER9sH2ek4fCyHSfM3M3nBFo7l5DGkR3Puu7AtLerX8jqaMaVSqQtE8+bNSUtLY+/evSWum52dHTYfiBWRNTo6mubNmwf1NSqbo8dzefP7rbz67SaOZOdyedcm3H9REmc2ivE6mjGnpVIXiMjIyFPONi7OvHnz6N69e5ATlY9wyloVZOfk8c6in3l53ib2Hz3BRR0SeODiJDo2reN1NGPKpFIXCGOC6URuPh8u3c4L32xk95Fszm8bzwMXJ9G9ZT2voxlTLqxAGFNKefnKxyt2MHFuKtsPHKNXq3pMGN6Nvm0alLyxMWHECoQxAcrPV2as2cWzs1PZtPcoXZrF8eTvO/ObpIY2CMJUSlYgjCmBqjJ3/R7GzU5l/a4jJCXE8MpNPfltpwQrDKZSswJhTBFUlYUb9zN2Vgortx8isUEtJg7vxuVdmxJhU2+bKsAKhDF+LN16gH/NTOHHLQdoVrcm/xzahSE9mhNpU2+bKsQKhDE+th7O49Z/L2Zeyl4axkbx+JWdGN6nBVHVbYZVU/VYgTBVkqqy63A2KekZpO7OICU9g5TdGazdmU3dWnk8dGl7bj4nkZo1rDCYqssKhKn0Dhw9QcruDFLTfykEqbszyDiee3KdxnWiSWocy7C2kYy5cSCx0TbDqjFWIEylkXk8lw3pbiHYnUlK+hFSdmeyL/P4yXXiakbSrnEsV3dvRlLjWNolxJKUEEPdWjUA5yx1Kw7GOKxAmLBzPDePzXuPuoXAvaVnkHbwl2ts14yMICkhhoHtGtKucSxJCbG0axxLo9goG5pqTICsQJiQlZevbDuQ9UvzkFsItuw7Sl6+Mx159WrCGQ1j6N6yHsN7tzhZCFrUq0U1G4pqTJlYgTCeU1V2H8k+5WggNT2DDemZHM/NB0AEWtavRVJCLIM6NT7ZPNQ6vjY1qtvQU2OCIagFQkQGAROBCGCSqj5TaHkrYDLQEDgA3KSqae6y/wMGA9WA2cB9alexCXsHj5442VHsO4IoI/uXDuNGsVG0axzLiL6tThaCtgkx1Kph32eMqUhB+4sTkQjgReBiIA1YIiKfqeo6n9XGAm+r6lsicgHwNDBCRM4F+gFd3fUWAL8B5gUrryl/x3PzmLF6F1+tP86kjT+Skp7B3oxfOozrRFenfeM6XNWtqdtZ7Nzq1a7hYWpjTIFgfiXrA2xU1c0AIjIFuArwLRAdgT+595OBT9z7CkQDNQABIoH0IGY15SgnL5/py9N4bu5Gdhw6Ro1q0L5pDr9JaugUAveoIKGOdRgbE8okWK02IjIMGKSqt7mPRwBnq+rdPuu8B/yoqhNFZAgwDYhX1f0iMha4DadAvKCq/+PnNUYBowASEhJ6Tpky5bTzZmZmEhMTHlf+CtWs+ar8uCuPTzaeID1LaRNXjSFtI2kZlU2d2NDL60+ovrdFCae84ZQVwitvWbIOHDhwmar28rtQVYNyA36H0+9Q8HgE8HyhdZoC04EVOH0VaUAccCbwJRDj3n4A+hf3ej179tSySE5OLtP2FSnUsubn5+tXq3fpxePnaau/faG/ffZbnbV2t+bn56tq6OUtTjhlVQ2vvOGUVTW88pYlK7BUi/hcDWYTUxrQwudxc2Cn7wqquhMYAiAiMcBQVT3sHhksUtVMd9lXQF/guyDmNaWkqnybupdxs1JZveMwbeJr8/z13RncpYkNMTWmEghmgVgCtBWR1sAOYDhwg+8KIhIPHFDVfOAhnBFNANuAkSLyNE4T02+ACUHMakpp0eb9jJuVwpKtB2leryb/GtaVa7o3o7rNdmpMpRG0AqGquSJyNzATZ5jrZFVdKyJP4BzSfAYMAJ4WEcU5Ohjtbj4VuABYjdNh/bWqfh6srCZwK7YdZPzsVOZv2EdCnSievLoz1/VqYeciGFMJBXVguarOAGYUeu5Rn/tTcYpB4e3ygNuDmc2UzrqdRxg/O4U56/dQv3YNHhncgZv6tiI60mY7NaaysjOPTLE27slkwpxUvli1i9jo6jx4SRK39mtNTJT91zGmsrO/cuPX9gNZTJy7genL04iOjODugWcy8vw2xNWymU6NqSqsQJhT7D6czQvJG/hgyXZEhD/0a80dA84gPibK62jGmApmBcIAsD/zOC/P28R/Fv1MXr4yvE8L7h7YlsZx0V5HM8Z4xApEFXc4K4fX529m8sItZOfkMaRHc+67sC0t6tfyOpoxxmNWIKqoo8dz+ffCLbz23WaOZOdyedcm3H9REmc2Co+pBYwxwWcFoorJzsnjnUU/89K8TRw4eoKLOjTigYvb0bFpHa+jGWNCjBWIKuJEbj4fLN3OC99sIP3Icc5vG88DFyfRvWU9r6MZY0KUFYhKLjcvn49X7GDi3A2kHTxGr1b1mDi8O33bNPA6mjEmxFmBqKTy85UvV+/i2TmpbN57lC7N4njq6s78JqmhXYPBGBMQKxCVjKoyZ/0exs1K4afdGSQlxPDKTT35bacEKwzGmFKxAlFJqCoLN+5n7KwUVm4/RGKDWkwc3o3LuzYlwqbeNsacBisQlcDSrQf418wUftxygKZx0fxzaBeG9GhOpE29bYwpAysQYWx12mHGzkrh29S9NIyN4vErOzG8TwuiqtsMq8aYsrMCEYbSMvK5/T9Lmbk2nbq1Inno0vbcfE4iNWtYYTDGlB8rEGHmubkbeHbhMWKicvjTRUn84bxEYqNthlVjTPmzAhFGPlmxg/GzU+nbJIKXbxtIvdo1vI5kjKnErECEiRXbDvLXaas4u3V9bmubbcXBGBN0NswlDOw6fIxR/1lGQp0oXr6pJ9Vt2KoxpgJYgQhxx07kMertZWQdz+WNW3pT344cjDEVxJqYQpiq8uDU/7Jm52Em3dyLpIRYryMZY6oQO4IIYc9/s5EvV+3ib4Pac2GHBK/jGGOqGCsQIeqr1bsYPzuVId2bcXv/Nl7HMcZUQdbEFILW7DjMAx/+l+4t6/K/Q7qE7yR7+XmwOZnoY/u9TmKMOQ1WIELMnoxsRr29lLq1Inl1RE+iI8P07OiDP8PHd8C27+kLsON16PI76HQNxDTyOp0xJgDWxBRCsnPyuP0/yziYlcPrN/eiUWy015FKTxVWvg8v94Pdq2HweDa1uQVysuGrv8K4dvD21bDiHcg+7HVaY0wx7AgiRKgqD3+8mhXbDvHSjT3o3CzO60ill3UAvrgf1n0KLc+Ba16Feq3YfnQeZwx4Dvb8BGumwuqp8Olo+OIBaHuxc2SR9FuIrOn1T2CM8RFQgRCRacBk4CtVzQ9upKrpte82M335Dv50URKXdWnidZzS2zgXPrkLsvbDhWOg331QrVDzWKP2cMEjMPB/YMdyp1ismQY/fQE1YqHD5dB5GLQZABH23cUYrwX6V/gy8HvgORH5CHhTVX8KXqyqZe76dJ75+icGd23CvRee6XWc0sk5BrPHwOJXIb4d3PghNDmr+G1EoHlP53bJU7B1vnNUse4z+O/7UCseOl3tHFk07wPVrCXUGC8EVCBUdQ4wR0TigOuB2SKyHXgdeEdVc4KYsVJLTc/g3vdX0KlpHcYOOyu8RiztXAnTR8G+FDj7DrjosdI3E1WLcI4Y2gyAweNg4xxY/RGseBeWTIK4FtB5KHQZBgmdneJijKkQAR/Hi0gD4CZgBLACeBc4D7gFGBCMcJXdgaMnuO2tpdSKqs7rN/cKn+s55OfBwgmQ/DTUjocRH8MZF5R9v9WjoP1g53Y8A36a4TRDff+883oN2ztNUF2GQn07N8SYYAu0D2I60B74D3CFqu5yF30gIkuDFa4yO5Gbz53vLGP3kWw+GNWXJnFh0kF7cKs7fPUH6Hg1XP4s1Kpf/q8TFQtnXefcju6HdZ84zVDJTzm3Zj1/GTYb27j8X98YE/ARxAuq+o2/BaraqxzzVAmqypjP1vLjlgNMuK4b3VvW8zpSyVSd/oEZf3Waea55FbpeVzFNPrUbQO8/OrdD22HtdKdYfP13mPkwJJ7vNEF1uAJqhsF7aUyYCLT3r4OI1C14ICL1ROSuIGWq9N7+4WfeX7yNOwecwdXdm3kdp2RZB+DDm+GTO6FJV7hzIZw13Jv+gLotnHcpR8EAABwHSURBVBFSd8yH0Uug/1/g8Hb47B4YmwTv3wBrpsOJrIrPZkwlE+gRxEhVfbHggaoeFJGRwEvBiVV5zd+wlye+WMdFHRrxl0vaeR2nZBvnwCejneGrFz0O597z6+GrXmmYBAMfhgEPwc7lsHqaM2w25UuoEeP0ZXT5nTts1i7LakxpBVogqomIqKoCiEgEYBcmKKXNezMZ/e5yzmwYw4Th3akWyhf+OZEFc8bA4tegYQe48SPn6CEUiTh9Es16wiVPws8LnZFQ6z6FVR9AzfpOX0WXYdCirw2bNSZAgRaImcCHIvIKoMAdwNdBS1UJHc7K4ba3llI9ohqTbulFTFQInwi2cyVMHwn7UqHvXc6Jb5FhMu1HtQho3d+5XTbWOYFvzVRY+R4sfQPqNIfOQ5wji8ZdbNisMcUI9FPqb8DtwJ2AALOASSVtJCKDgIlABDBJVZ8ptLwVzhnaDYEDwE2qmuYua+m+RguconSZqm4NMG9Iyc3L5+73l7P9YBbv/PFsWtSv5XUk//LzYMGzMO9pqN0IRnwCZwz0OtXpqx4F7S9zbsczIeUr58hi0Uvw/XMQn+QUis5DocEZXqc1JuQEeqJcPs7Z1C8HumO3GepF4GIgDVgiIp+p6jqf1cYCb6vqWyJyAfA0znkWAG8D/1DV2SISA4TtFB//mLGe+Rv28c+hXTi7TQOv4/h3cCtMvx22L3KaYwaPD87wVa9ExUDX3zm3rAPusNlpkPwP59a0B3QZRkxGTdgd73XawFSrDprndQpTiQV6HkRbnA/vjsDJtgZVLe5spT7ARlXd7O5jCnAV4FsgOgJ/cu8nA5+463YEqqvqbPd1MgPJGYreX7yNfy/cyh/6tea63i29jvNrqrDyXfjqbyDV4JrXoOu1lbvppVZ96PUH53Z4hzts9iOY+TC9AJZ5HTBw59SoB8evd/pXmvao3L83U+HE7XcufiWRBcAY4FngCpx5mURVxxSzzTBgkKre5j4eAZytqnf7rPMe8KOqThSRIcA0IB44H7gNOAG0BuYAf1c99euSiIwCRgEkJCT0nDJlSqA/969kZmYSExNz2tv789OBPP61JJsODSL4U48oIsqpU7q8skaeOEJS6os03LeIQ3GdWd/hPo5Hl/+1GoLx3gZDzaw0IvZvIDo6PPpbIvKOUXf3QhIOr6Sa5pJVswl7Gp3Pnkb9yardwut4vxIu/w8KhFPesmQdOHDgsiLPZ1PVEm/AMvff1T7PzS9hm9/h9DsUPB4BPF9onabAdJypOybiNEXFAcOAw0AbnKOcacAfi3u9nj17alkkJyeXafvCtu0/qt0en6kDxybroawT5brvcsmaOkv1X21VH2+gumCCal5u2fdZhPJ+b4MpnLKqunmzDqoue1v1rStVH6urOqaO6sv9VOc/q3pwm9cRTwrL9zZMlCUrsFSL+FwNtJM6W0SqARtE5G5gB1DSV800nA7mAs2BnYWK005gCIDbzzBUVQ+LSBqwQn9pnvoE6Au8EWBeT2Uez+W2t5aSr/DGLb2JqxlCY/BPZMHs/+dMhNewA9w0zRnNY8JXzbrQY4Rzy0iHtR87TWZzxji3luc681d1vMY5K92YAAU6IPx+oBZwL9ATZ9K+W0rYZgnQVkRai0gNYDjwme8KIhLvFh6Ah3BGNBVsW09EGrqPL+DUvouQlZev3D9lBRv3ZvLiDT1oHV/b60i/2LEcXu3vFIe+o2HUPCsOlU1sAvS9A0bOhXtXONffOHYAvvwzjEuCd4bBfz9wJkM0pgQlHkG4o5GuVdW/AJk4/Q8lUtVc92hjJs4w18mqulZEnsA5pPkMZxbYp0VEge+A0e62eSLyIDBXnPmvl+FMLR7yxs5KYc76PTx+ZSfOaxsio2Hycp3hq98+4wxfvflT5+xiU7nVb+NMRXL+g5C+1r2a3zT4eBRUrwntBjmz47a92BkSbEwhJRYI98O6p++Z1IFS1RnAjELPPepzfyowtYhtZwMheuqufx+vSOPleZu44eyW3HxOK6/jOA5sdoavpi12xvsPHmcT2lU1ItC4s3O74FFIW+I0Qa392LlFxUHHK5xzQhLPD52pVIznAu2DWAF86l5N7mjBk6o6PSipwtDybQf527TV9G1Tn8ev7OT9hX9UYcV/4OuHQCJgyCTnHABTtVWrBi3Pdm6DnoEt85yZcdd+CivegZgE6DTEGTbbrKcNm63iAi0Q9YH9OH0BBRRnBFKVt/PQMUa9vYzGdaJ5+caeREZ4PNfP0X3w+X3OtZ4Tz4erX3ZmQTXGV0R1OPMi53b5MUid6TRDLZ0MP74M9RLdCzT9zrmeuKlyAj2TOqB+h6oo60QuI99eSnZOHu+NPJt6tT2ewzB1Fnw6GrIPOdd77jvaJqczJYus6VwHvNPVkH0Y1n/hNEMtGA/zx0JCF2ckVOehUDcET/g0QRHomdT/xjliOIWq/qHcE4WR/HzlwY/+y7pdR3jjll4kJcR6F+bEUZj1iPPtr1FH5zKgjTt7l8eEr+g46H6jc8vc4w6bnQpzHnNuLfo6TVCdrnEuOWsqrUCbmL7wuR8NXEOhcxqqoue+2cCM1bt5+LL2XNA+wbsgO5bB9FGwfyOcczdc8P/CZ/ZVE9piGsHZtzu3g1ud622sngozHnSmZzljoNMM1X4wRNfxOq0pZ4E2MU3zfSwi7+NMf1FlfblqFxPmbGBoj+aMPL+4KamCKC/XaQKY94xzXeabP4M2v/Emi6n86iXC+X92bulrnUKxZip8cgdUj4ak3zr9FWdebF9QKonTvShBW6DKNkSu2XGYP3+0kh4t6/K/Qzp7M2LpwGbnqCFtifMNbvBYG75qKk5CJ+d2YaFhs+s+hag60OFKp88isb/TGW7CUqB9EBmc2gexG+caEVXOnoxsRr69lPq1avDqiF5EVa/gMeOqNNk5Cxa+6Uz3PPQNpz3YGC+IQIs+zu23T8OWb51mqPWfwcp3nBMzO13jHFmU7jQqEwICbWLysPc1dGTn5HH7f5ZxKCuHqXeeQ8NYD84+Tf5f2qW+6AxfveYViGte8RmM8SeiOpx5oXMbPB42zHKOLJa9CYtfpb9EwILwOQmvf34+zA+PEYDdYs6EAT+U+34DPYK4BvhGVQ+7j+sCA1T1k3JPFKJUlYenr2bFtkO8clMPOjWNq/gQWQfghxfY0/BcGt38mQ1fNaErMho6Xuncsg/DT1+yffkcWrUMn5bp7du2hU3ePelZ1A3CfgNtHByjqh8XPFDVQyIyBvcCP1XBq99tZvqKHTxwcRKDOjfxJsSPr0BOFlsTr6eRFQcTLqLjoNsNbDnUlFYDBnidJmBb5s0Lm7w7580jKQj7DfRTxt96Vabnac66dP759U9c3rUJ91xwpjchjmc4BaL95WTVDo9vNcaY8BZogVgqIuNF5AwRaSMizxJWF2Y8fSm7M7hvygo6N43jX8PO8m6OpaWTnUP18x/w5vWNMVVOoAXiHpzLf34AfAgcw52auzLbn3mcP761hNpR1Xn95l7UrOFRB1tONnz/ArQZ6EygZowxFSDQUUxHgb8HOUtIOZGbz53vLmdPxnE+vP0cGsd5eOLPynfg6B44f3LJ6xpjTDkJ6AhCRGa7I5cKHtcTkZnBi+UtVeXRT9eweMsB/jWsK91aBGN8QIDycmDhRGjeBxLP8y6HMabKCbSJKV5VDxU8UNWDlHxN6rD15vdbmbJkO6MHnsFV3Zp5G2bNNDi0zZnewObmN8ZUoEALRL6InBw6IyKJ+JndtTL4LnUvT36xjos7JvDni9t5GyY/H+aPh4TOzjw3xhhTgQIdqvo/wAIR+dZ93B8YFZxI3tm0N5PR7y0nKSGWCdd1o1o1j7+xp3wJ+1Kc6TTs6MEYU8EC7aT+WkR64RSFlcCnOCOZKo2jOcrIt5ZSI6Iak27pRe0oj0/zUIX545wLz3e6xtssxpgqKdCpNm4D7gOa4xSIvsAPnHoJ0rCVm5fPSyuz2X5IeW9kX5rXq+V1JNicDDtXwBXP2UXkjTGeCLQP4j6gN/Czqg4EugN7g5aqgj315XrW7s/nqas70zuxvtdxHPPHQ2xTOGu410mMMVVUoAUiW1WzAUQkSlV/AjzuwS0fm/Zm8s6in/ltq+pc1ztEprDY9iNsnQ/n3gPVPZgx1hhjCLyTOs09D+ITYLaIHKSSXHL0jIYxfDK6H+kpy72O8osF46Fmfeh5i9dJjDFVWKCd1AW9pI+JSDIQB3wdtFQVrHOzOPZtCJFRQrtXQ+rXMPARqFHb6zTGmCqs1EN1VPXbktcyp23Bs1AjFvrc5nUSY0wVZxcVCCX7NznX9e39R7u+tDHGc1YgQsnCCRBRA86p9BPlGmPCgBWIUHF4B6x8H7qPgJhKO82VMSaMWIEIFT+8ACj0u9frJMYYA1iBCA1H98GyN6HLtVA3RM7FMMZUeVYgQsGPr0DOMTjvfq+TGGPMSVYgvJZ9BH58DTpcAQ0rxcnpxphKwgqE15a+AccPw/kPeJ3EGGNOYQXCSznH4IcX4YwLoWl3r9MYY8wprEB4afl/4Ohe53KixhgTYqxAeCX3BCycCC36QqtzvU5jjDG/EtQCISKDRCRFRDaKyN/9LG8lInNFZJWIzBOR5oWW1xGRHSLyQjBzemL1R3AkzTl6sMuJGmNCUNAKhIhEAC8ClwIdgetFpGOh1cYCb6tqV+AJ4OlCy58EKt/kgPl5zqR8CV2g7cVepzHGGL+CeQTRB9ioqptV9QQwBbiq0Dodgbnu/WTf5SLSE0gAZgUxozfWfw77Nzgjl+zowRgTokRVg7NjkWHAIFW9zX08AjhbVe/2Wec94EdVnSgiQ4BpQDxwEPgGGAFcCPTy3c5n+1HAKICEhISeU6ZMOe28mZmZxMTEnPb2AVOl57IHiMjLZnGfF0BKf73pCstaTsIpbzhlhfDKG05ZIbzyliXrwIEDl6lqL78LVTUoN+B3wCSfxyOA5wut0xSYDqwAJgJpOBcjuhv4q7vOrcALJb1ez549tSySk5PLtH3AUmerjqmjuuzt095FhWUtJ+GUN5yyqoZX3nDKqhpeecuSFViqRXyulvqCQaWQBrTwedycQpcpVdWdwBAAEYkBhqrqYRE5BzhfRO4CYoAaIpKpqr/q6A4788dBnWbQ9TqvkxhjTLGCWSCWAG1FpDWwAxgO3OC7gojEAwdUNR94CJgMoKo3+qxzK04TU/gXh5+/h23fw6B/QvUaXqcxxphiBa2TWlVzcZqKZgLrgQ9Vda2IPCEiV7qrDQBSRCQVp0P6H8HKExLmj4daDaDHzV4nMcaYEgXzCAJVnQHMKPTcoz73pwJTS9jHm8CbQYhXsXb9FzbOhgv+H9So5XUaY4wpkZ1JXVHmj4eoOtD7Nq+TGGNMQKxAVIR9G2Ddp05xqFnX6zTGGBMQKxAVYcEEqB4Ffe/yOokxxgTMCkSwHdoOq6ZAj1sgpqHXaYwxJmBWIILt++edf8+9x9scxhhTSlYggilzLyx/C7oOh7otSl7fGGNCiBWIYFr0EuQeh/Pu9zqJMcaUmhWIYDl2CJZMgo5XQXxbr9MYY0ypWYEIliWT4PgRZ0pvY4wJQ1YgguFEltO8dObF0OQsr9MYY8xpsQIRDMvfhqz9zuVEjTEmTFmBKG+5J+D756DludDqHK/TGGPMabMCUd5WfQBHdtjRgzEm7FmBKE/5ebDgWWjcFc680Os0xhhTJlYgytO6T+HAJufoQcTrNMYYUyZWIMqLqjOld4O20OEKr9MYY0yZWYEoLxtmQ/pqOO9PUC3C6zTGGFNmViDKgyrMHwtxLaDrtV6nMcaYcmEFojz8/D1s/xHOvRciIr1OY4wx5cIKRHmYPw5qN4QeI7xOYowx5cYKRFntXAGb5jpXi4us6XUaY4wpN1Ygymr+eIiKg95/9DqJMcaUKysQZbE3BdZ/Dn1GQnSc12mMMaZcWYEoiwUToHo09L3T6yTGGFPurECcroM/O/Mu9bwVasd7ncYYY8qdFYjT9f3zINXg3Lu9TmKMMUFhBeJ0ZKQ713w4azjENfc6jTHGBIUViNOx6CXIz3Gm1TDGmErKCkRpHTsIS96AjldDgzO8TmOMMUFjBaK0Fk+CExlw/gNeJzHGmKCyAlEaJ446zUttfwuNu3idxhhjgsoKRGksewuOHbDLiRpjqgQrEIHKPe4MbW11HrQ82+s0xhgTdFYgAvXfKZCx0/oejDFVhhWIQOTlwoJnoUk3OOMCr9MYY0yFsAIRiHWfwMEtTt+DiNdpjDGmQliBKImqM6V3fBK0v9zrNMYYU2GCWiBEZJCIpIjIRhH5u5/lrURkroisEpF5ItLcfb6biPwgImvdZdcFM2exUmfCnrVw3gNQzeqpMabqCNonnohEAC8ClwIdgetFpGOh1cYCb6tqV+AJ4Gn3+SzgZlXtBAwCJohI3WBlLZIqzB8LcS2hy7AKf3ljjPFSML8S9wE2qupmVT0BTAGuKrROR2Cuez+5YLmqpqrqBvf+TmAP0DCIWf3bugDSlkC/eyEissJf3hhjvCSqGpwdiwwDBqnqbe7jEcDZqnq3zzrvAT+q6kQRGQJMA+JVdb/POn2At4BOqppf6DVGAaMAEhISek6ZMuW082ZmZhITE3PKc13/O4aYzK0s6vsa+RFRp73v8uYvaygLp7zhlBXCK284ZYXwyluWrAMHDlymqr38LlTVoNyA3wGTfB6PAJ4vtE5TYDqwApgIpAFxPsubAClA35Jer2fPnloWycnJpz6RtlR1TB3V+c+Wab/B8KusIS6c8oZTVtXwyhtOWVXDK29ZsgJLtYjP1eqnVXICkwa08HncHNhZqDjtBIYAiEgMMFRVD7uP6wBfAo+o6qIg5vRv/njnOtO9/lDhL22MMaEgmH0QS4C2ItJaRGoAw4HPfFcQkXgRKcjwEDDZfb4G8DFOB/ZHQczo356f4KcvoM/tEF2nwl/eGGNCQdAKhKrmAncDM4H1wIequlZEnhCRK93VBgApIpIKJAD/cJ+/FugP3CoiK91bt2Bl/ZUFz0JkLTj7jgp7SWOMCTXBbGJCVWcAMwo996jP/anAVD/bvQO8E8xsRTq4FVZ/5BSH2g08iWCMMaHAzvwqbOFzINXg3LtLXtcYYyoxKxC+MnbDineg2w1Qp6nXaYwxxlNWIHz98CLk50C/+7xOYowxnrMC4aqekwFLJ0OnIdDgDK/jGGOM56xAuJrt+BJOZMJ5f/I6ijHGhAQrEADHM2me9gUkXQqNO3udxhhjQoIVCIBlbxKZm+FcEMgYYwxgBQJyj8P3z3Owbhdo0dvrNMYYEzKCeqJcWMjcA/Vbs63uIOp5ncUYY0KIHUHUbQF/+JqD9c7yOokxxoQUKxAFRLxOYIwxIcUKhDHGGL+sQBhjjPHLCoQxxhi/rEAYY4zxywqEMcYYv6xAGGOM8csKhDHGGL9EVb3OUC5EZC/wcxl2EQ/sK6c4wRZOWSG88oZTVgivvOGUFcIrb1mytlLVhv4WVJoCUVYislRVe3mdIxDhlBXCK284ZYXwyhtOWSG88gYrqzUxGWOM8csKhDHGGL+sQPziNa8DlEI4ZYXwyhtOWSG88oZTVgivvEHJan0Qxhhj/LIjCGOMMX5ZgTDGGONXlS8QIjJZRPaIyBqvs5RERFqISLKIrBeRtSJyn9eZiiIi0SKyWET+62Z93OtMJRGRCBFZISJfeJ2lJCKyVURWi8hKEVnqdZ6SiEhdEZkqIj+5/3/P8TqTPyLSzn1PC25HROR+r3MVR0T+5P6NrRGR90Ukutz2XdX7IESkP5AJvK2qnb3OUxwRaQI0UdXlIhILLAOuVtV1Hkf7FRERoLaqZopIJLAAuE9VF3kcrUgi8gDQC6ijqpd7nac4IrIV6KWqYXEil4i8BcxX1UkiUgOopaqHvM5VHBGJAHYAZ6tqWU7CDRoRaYbzt9VRVY+JyIfADFV9szz2X+WPIFT1O+CA1zkCoaq7VHW5ez8DWA808zaVf+rIdB9GureQ/TYiIs2BwcAkr7NUNiJSB+gPvAGgqidCvTi4LgQ2hWpx8FEdqCki1YFawM7y2nGVLxDhSkQSge7Aj94mKZrbZLMS2APMVtWQzQpMAP4K5HsdJEAKzBKRZSIyyuswJWgD7AX+7TbhTRKR2l6HCsBw4H2vQxRHVXcAY4FtwC7gsKrOKq/9W4EIQyISA0wD7lfVI17nKYqq5qlqN6A50EdEQrIJT0QuB/ao6jKvs5RCP1XtAVwKjHabSkNVdaAH8LKqdgeOAn/3NlLx3GawK4GPvM5SHBGpB1wFtAaaArVF5Kby2r8ViDDjtudPA95V1ele5wmE25wwDxjkcZSi9AOudNv1pwAXiMg73kYqnqrudP/dA3wM9PE2UbHSgDSfI8ipOAUjlF0KLFfVdK+DlOAiYIuq7lXVHGA6cG557dwKRBhxO37fANar6niv8xRHRBqKSF33fk2c/8g/eZvKP1V9SFWbq2oiTrPCN6pabt/CypuI1HYHKeA21VwChOwoPFXdDWwXkXbuUxcCITewopDrCfHmJdc2oK+I1HI/Hy7E6ZssF1W+QIjI+8APQDsRSRORP3qdqRj9gBE433ALhuFd5nWoIjQBkkVkFbAEpw8i5IePhokEYIGI/BdYDHypql97nKkk9wDvuv8fugH/63GeIolILeBinG/jIc09KpsKLAdW43yml9u0G1V+mKsxxhj/qvwRhDHGGP+sQBhjjPHLCoQxxhi/rEAYY4zxywqEMcYYv6xAGGOM8csKhDEVzJ2qO/40t71VRJqWx76MKYkVCGPCy604c+4YE3RWIEyVJSKJ7gVsJrkXW3lXRC4SkYUiskFE+ri3791ZSL8vmC5CRB4Qkcnu/S7u9rWKeJ0GIjLL3cergPgsu8m9sNJKEXnVvQYBIpIpIuNEZLmIzHWnLhmGc72Kd931a7q7ucddb7WItA/me2aqFisQpqo7E5gIdAXaAzcA5wEPAg/jzB/V352F9FF+mSJiAnCmiFwD/Bu4XVWziniNMcACdx+fAS0BRKQDcB3OzKzdgDzgRneb2jiTxfUAvgXGqOpUYClwo6p2U9Vj7rr73PVednMbUy6qex3AGI9tUdXVACKyFpirqioiq4FEIA54S0Ta4lyDIRJAVfNF5FZgFfCqqi4s5jX6A0Pc7b4UkYPu8xcCPYElzjxr1MS5dgY416X4wL3/DsXPC1SwbFnB6xhTHqxAmKruuM/9fJ/H+Th/H08Cyap6jXuRpnk+67fFuVxtIH0C/iY9E+AtVX3oNLcvUJA5D/ubNuXImpiMKV4cznWJwekgBkBE4nCapvoDDdz+gaJ8h9t0JCKXAvXc5+cCw0Skkbusvoi0cpdVAwr2eQPOdYcBMoDYMvw8xgTMCoQxxfs/4GkRWQhE+Dz/LPCSqqYCfwSeKfig9+NxoL+ILMe5dsM2AFVdBzyCc+nQVcBsnGnSwbnqWicRWQZcADzhPv8m8EqhTmpjgsKm+zYmBIlIpqrGeJ3DVG12BGGMMcYvO4IwppyIyO+B+wo9vVBVR3uRx5iysgJhjDHGL2tiMsYY45cVCGOMMX5ZgTDGGOOXFQhjjDF+/X+ig3XcLmdYYgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt \n",
    "%matplotlib inline\n",
    "plt.plot(max_depth_values,train_accuracy_values,label='acc train')\n",
    "plt.plot(max_depth_values,val_accuracy_values,label='val train')\n",
    "plt.legend()\n",
    "plt.grid(axis='both')\n",
    "plt.xlabel(\"max_depth\")\n",
    "plt.ylabel(\"accuracy\")\n",
    "plt.title(\"effect of max depth acuuracy\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(ccp_alpha=0.0, class_weight=None, criterion='gini',\n",
       "                       max_depth=3, max_features=None, max_leaf_nodes=None,\n",
       "                       min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "                       min_samples_leaf=1, min_samples_split=2,\n",
       "                       min_weight_fraction_leaf=0.0, presort='deprecated',\n",
       "                       random_state=2, splitter='best')"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model_best=DecisionTreeClassifier(max_depth=3,random_state=2)\n",
    "model_best.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Test:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9292035398230089\n"
     ]
    }
   ],
   "source": [
    "y_pred_test=model_best.predict(x_test)\n",
    "print(accuracy_score(y_test,y_pred_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_____________________\n",
    "Display the effiecient features with bar:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.02340327, 0.83879425, 0.05794766, 0.        , 0.        ,\n",
       "       0.06737306, 0.01248175, 0.        , 0.        ])"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model_best.feature_importances_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "feature_names=[\n",
    "     \n",
    "    \"Clump Thickness\",\n",
    "     \"Uniformity of Cell Size\",\n",
    "     \"Uniformity of Cell Shape\",\n",
    "     \"Marginal Adhesion\",\n",
    "     \"Single Epithelial Cell Size\",\n",
    "     \"Bare Nuclei\",\n",
    "     \"Bland Chromatin\",\n",
    "     \"Normal Nucleoli\",\n",
    "     \"Mitoses\",\n",
    "     ]\n",
    "plt.bar(feature_names, model_best.feature_importances_)\n",
    "\n",
    "\n",
    "\n",
    "plt.xlabel('features')\n",
    "plt.xticks(rotation=90)\n",
    "plt.ylabel('importances')\n",
    "plt.title('feature importances')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the shape of tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x1080 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(20,15))\n",
    "from sklearn import tree\n",
    "tree.plot_tree(model_best,feature_names=[\n",
    "     \n",
    "    \"Clump Thickness\",\n",
    "     \"Uniformity of Cell Size\",\n",
    "     \"Uniformity of Cell Shape\",\n",
    "     \"Marginal Adhesion\",\n",
    "     \"Single Epithelial Cell Size\",\n",
    "     \"Bare Nuclei\",\n",
    "     \"Bland Chromatin\",\n",
    "     \"Normal Nucleoli\",\n",
    "     \"Mitoses\",\n",
    "     ],class_names=[\"benign\",\"maligment\"],filled=True)\n",
    "plt.show()"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
