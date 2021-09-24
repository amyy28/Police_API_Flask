# PoliceAPI Flask
This is an API which returns a list of nearest police stations within a range of 1km from the entered location.
Uses Google Nearby Places API and Geocoding API. Thus GCP account is mandatory.

## Instructions to use
Make sure your GCP account is setup and an API key is ready with both the above API's enabled in the google cloud platform. 

### Clone the repository
```
git clone https://github.com/amyy28/Police_API_Flask.git
```

### Install all the dependencies at once
```
pip3 install -r requirements.txt
```

#### Replace API_KEY in the main.py file with your own ready API_KEY.

### Now run the flask file
```
python3 app.py
```

Now hit on the localhost URL and give the location as :
```
/policestations/<location name>
```
The API will return the results.

#### Below API request can also be checked on Postman.


print(mean_squared_error(yy_test, RF_multi.predict(X_test_all)))
preds = np.stack([t.predict(X_test_all) for t in RF_multi.estimators_])
preds[:,0], np.mean(preds[:,0]), yy_test
plt.plot([r2_score(yy_test, np.mean(preds[:i+1], axis=0)) for i in range(100)]);
