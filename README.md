# Detecting fake news using DistilBERT

### Detection is based on collection of Twitter posts which contain rumours or non-rumours (fake & real) information.
In addition to analyzing plain text of each tweet graph data (social interactions) is taken into consideration, e.g. retweet count, shares count, etc.

## Setup
1. Create venv with your favourite tool
2. Activate it
3. Run 
```bash
   python install.py
```
4. Provide `dataset.key` file in **raw** directory
5. In **raw** directory run
```bash
bash prepare_dataset.sh  # This will initialize raw dataset
```
6. Run
```bash
python setup_dataset.py  # This will create dataset.csv
```


## Credits & acknowledgements
Original dataset (*PHEME*) belongs to `Elena Kochkina`, `Maria Liakata` & `Arkaitz Zubiaga`.<br>
It was downloaded from [here](https://figshare.com) and then encrypted because of sensitive data inside.