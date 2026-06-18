15/06/2026
- planning on complete overview of project completed

16/06/2026
- Realised only removing same song IDs is not sufficient to remove all duplicates
had to also remove songs that had the same exact artist and same exact song name
- Chose standardisation rather than normalisation because some attributes contain outliers and KNN relies on distance calculations.

- Original dataset: 114000 songs
- Unique track IDs: 89741
- Significant number of duplicates removed

- reasoned about similaity features that should be taken into consideration for song recommendations 

17/06/2026
- Implemented version 1 of KNN song recommendation system
- Songs suggested were all mathematically similar
- Tested out model with wide range of songs such as Drake's One Dance and God's Plan, Mac Miller's cinderella and the songs suggested 
were all really good. Suggested songs broke the language barrier and even genre barrier that is usually faced
when trying to find similar songs - helped discover new artists and even new genres
    - Enter song name: One Dance
Enter artist name: Drake;Wizkid;Kyla
           track_name                                artists
41188       One Dance                      Drake;Wizkid;Kyla
33270        Badabing                   buller;LKN;El Chilli
18364     Your Matter                   Seyi Shay;Eugy;Efosa
44553  Cate's Brother                          Maisie Peters
51804   Somos Iguales  Ozuna;Tokischa;Louchie Lou;Michie One
321    Slow Down Time                             Us The Duo
- I found that equal weighting of all features produced reasonable results, but I plan to allow users to adjust feature importance to make it more tailored for the user
- using a small dataset that is 4 years old so perhaps using spotify's api later on will lead to better and more accurate song recommendations
    - noticed some songs suggested were not available on spotify anymore

- recommendation judged accurate for now
- starting off with smaller dataset leads to new discoveries of song taste

18/06/2026
- manual playlist style query
    - find average song attribute values and find similar songs to average
    - setting up for future where user enters spotify public playlist link and program will find suggestions
    for the playlist