import numpy as np
import pandas as pd 
import matplotlib.lines as mlines
import matplotlib.pyplot as pyplot 
from sklearn.cluster import KMeans 
import colorsys
import random
import os
from matplotlib.mlab import PCA as mlabPCA
from matplotlib import pyplot as plt
from Tkinter import Tk
from tkFileDialog import askopenfilename



def get_colors(num_colors):
			    """
			    Function to generate a list of randomly generated colors
			    The function first generates 256 different colors and then
			    we randomly select the number of colors required from it
			    num_colors        -> Number of colors to generate
			    colors            -> Consists of 256 different colors
			    random_colors     -> Randomly returns required(num_color) colors
			    """
			    colors = []
			    random_colors = []
			    # Generate 256 different colors and choose num_clors randomly
			    for i in np.arange(0., 360., 360. / 256.):
				hue = i / 360.
				lightness = (50 + np.random.rand() * 10) / 100.
				saturation = (90 + np.random.rand() * 10) / 100.
				colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))

			    for i in range(0, num_colors):
				random_colors.append(colors[random.randint(0, len(colors) - 1)])
			    return random_colors


def random_centroid_selector(total_clusters , clusters_plotted):
			    """
			    Function to generate a list of randomly selected
			    centroids to plot on the output png
			    total_clusters        -> Total number of clusters
			    clusters_plotted      -> Number of clusters to plot
			    random_list           -> Contains the index of clusters
						     to be plotted
			    """
			    random_list = []
			    for i in range(0 , clusters_plotted):
				random_list.append(random.randint(0, total_clusters - 1))
			    return random_list

def plot_cluster(kmeansdata, centroid_list, label_list , num_cluster):
			    """
			    Function to convert the n-dimensional cluster to 
			    2-dimensional cluster and plotting 50 random clusters
			    file%d.png    -> file where the output is stored indexed
					     by first available file index
					     e.g. file1.png , file2.png ...
			    """
			    mlab_pca = mlabPCA(kmeansdata)
			    cutoff = mlab_pca.fracs[1]
			    users_2d = mlab_pca.project(kmeansdata, minfrac=cutoff)
			    centroids_2d = mlab_pca.project(centroid_list, minfrac=cutoff)


			    colors = get_colors(num_cluster)

			   	

			    plt.figure()
			    plt.xlim([users_2d[:, 0].min() - 3, users_2d[:, 0].max() + 3])
			    plt.ylim([users_2d[:, 1].min() - 3, users_2d[:, 1].max() + 3])
	

			    # Plotting 50 clusters only for now
			    random_list = random_centroid_selector(num_cluster , 50)

			    # Plotting only the centroids which were randomly_selected
			    # Centroids are represented as a large 'o' marker
			    for i, position in enumerate(centroids_2d):
				if i in random_list:
				    plt.scatter(centroids_2d[i, 0], centroids_2d[i, 1], marker='o', c=colors[i], s=100)



			    for i, position in enumerate(label_list):
				if i in label_list:
				    plt.text(centroids_2d[i, 0], centroids_2d[i, 1], str(i), color="red", fontsize=20)			

				 	
			    # Plotting only the points whose centers were plotted
			    # Points are represented as a small '+' marker
			    for i, position in enumerate(label_list):
				if position in random_list:
				    plt.scatter(users_2d[i, 0], users_2d[i, 1] , marker='+' , c=colors[position])
		
			    filename = "resultat"
			    i=0	
			    
			    plt.savefig(filename + ".png")

			    return


def ask_file1():
				global file1 

				Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing



				file1 = askopenfilename() # show an "Open" dialog box and return the path to the selected file

				return 


def ask_file2():
				global file2 
					
				Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
				



				file2 = askopenfilename()

				return 

def ask_file3():
				
				global file3
	
				Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

				file3 = askopenfilename()

				return 

def join_files():
				
			     	global ds 


				dataset1 = pd.read_csv(file1, delimiter=";",keep_default_na=False, na_values=[""])
				dataset2= pd.read_csv(file2,delimiter=";", keep_default_na=False, na_values=[""])
				dataset3= pd.read_csv(file3,delimiter=";", keep_default_na=False, na_values=[""])


				dataset0 = pd.merge(dataset1,dataset3,on="MATRICULE")
				dataset0 = pd.merge(dataset0,dataset2,on="MATRICULE")
				
				ds=dataset0
	
				return dataset0

def kmeans_apply():	
				
				global ds 
				global labels 
				global centroids

				dataset=ds.iloc[:,1:].values 

				k_means = KMeans(init='k-means++', n_clusters=3, n_init=500)
				k_means.fit(dataset)

				labels = k_means.labels_
				centroids = k_means.cluster_centers_


				plot_cluster(dataset, centroids, labels , 3)
				
								
				
				return 


def create_reporte(dataset,labels):
				

				datasetx=dataset.iloc[:,:].values 

				for i in range(3):
					print("group " + str(i))
					print(datasetx[np.where(labels==i),0])
	
				return 





