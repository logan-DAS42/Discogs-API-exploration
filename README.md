## Discogs API Exploration for App Development
This repo is still young, and only contains preliminary exploration of the Discogs API.

Discogs is a network, marketplace and database for discography data. Users are able to make profiles and track their physical media music collection by adding different releases to their collection. Community admins are allowed to edit and create master releases and their corresponding sub-releases, and therefore maintain the integrity of the discography records. The marketplace platform allows users to buy, sell and trade physical media, and is therefore a rich resource for extracting current market data on nearly any physical music media product.

#### Goals
  * create a method for recalling historical market data for a given release of a product with only the input of a SKU or barcode
      * find another uniform way for input besides SKU or barcode for releases prior to 1963 (potentially catalog number and publishing label)
  * contruct automated API querry for input of SKU or barcode
