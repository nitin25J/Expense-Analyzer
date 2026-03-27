from sklearn.cluster import KMeans

def clustering(data):
    model = KMeans(n_clusters=3, random_state=42, n_init=10)

    data['cluster'] = model.fit_predict(
        data[['rent', 'food', 'lifestyle']]
    )

    return data, model