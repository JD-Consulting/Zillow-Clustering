JD Consulting
 
 
|      	|                              	|                                       ORIGINAL FEATURES:                                      	|
|------	|------------------------------	|:---------------------------------------------------------------------------------------------:	|
| i    	| parcelid                     	| identification: numerical id assigned to a parcel region                                      	|
| ii   	| logerror                     	| difference between the actual sale price and the predicted sales pri                          	|
| iii  	| transactiondate              	| date a transaction took place                                                                 	|
| iv   	| bathroomcnt                  	| number of bathrooms a structure houses                                                        	|
| v    	| bedroomcnt                   	| number of bedrooms a structure houses                                                         	|
| vi   	| calculatedfinishedsquarefeet 	| calculated square feet of a completed structure                                               	|
| vii  	| latitude                     	| measurement: angular distance of location, north or south of the equator                      	|
| viii 	| longitude                    	| measurement: angular distance of location, east or west of the meridian at Greenwich, England 	|
| ix   	| lotsizesquarefeet            	| measurement: square foot size of the properties land                                          	|
| x    	| regionidcity                 	| identification: numerical id assigned                                                         	|
| xi   	| regionidzip                  	| identification: numerical zip code                                                            	|
| xii  	| yearbuilt                    	| date: year the structure was completed                                                        	|
| xiii 	| structuretaxvaluedollarcnt   	| monetary: tax value of the structure minus the land value                                     	|
| xiv  	| taxvaluedollarcnt            	| monetary: tax value of the structure and land combined                                        	|
| xv   	| landtaxvaluedollarcnt        	| monetary: tax value of the land minus the structure value                                     	|
| xvi  	| taxamount                    	| monetary: dollar amount of taxes                                                              	|
|      	|                              	|                                                                                               	|
|      	|                              	|                                     **CREATED FEATURES:**                                     	|
| i    	| LA                           	| county_name: assigned a 1 if True, otherwise 0                                                	|
| ii   	| Orange                       	| county_name: assigned a 1 if True, otherwise 0                                                	|
| iii  	| Ventura                      	| county_name: assigned a 1 if True, otherwise 0                                                	|
| iv   	| bed_bath_ratio               	| percentage: bathroomcnt / bedroomcnt                                                          	|
| v    	| tax_rate                     	| percentage: taxamount / taxvaluedollarcnt                                                     	|