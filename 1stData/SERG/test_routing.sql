SELECT
    *
FROM
    shortest_path_astar(
        'SELECT edge_id AS id, vertex_id1 AS source, vertex_id2 AS target, ' ||
        '(CASE WHEN door = ''S'' THEN -1.0                                                             
             ELSE                                                                                               
                 (length * (CASE network WHEN ''0''  THEN 1.0                                                     
                                         WHEN ''10'' THEN 1.2                                                     
                                         WHEN ''20'' THEN 1.5                                                     
                                         WHEN ''30'' THEN 2.0                                                     
                                         ELSE 1.0                                                               
                            END) *                                                                              
                           (CASE type    WHEN ''9.1'' THEN CASE WHEN level1 < level2 THEN  3.0 ELSE  2.0 END      
                                         WHEN ''9.2'' THEN CASE WHEN level1 < level2 THEN 15.0 ELSE 12.0 END      
                                         ELSE 1.0                                                               
                            END) +                                                                              
                           (CASE type    WHEN ''9.3'' THEN 40.0                                                   
                                         ELSE 0.0                                                               
                            END)                                                                                
                 )                                                                                              
        END)::float8 AS cost, ' ||
        '(CASE WHEN door_rev = ''S'' THEN -1.0                                                         
             ELSE                                                                                               
                 (length * (CASE network WHEN ''0''  THEN 1.0                                                     
                                         WHEN ''10'' THEN 1.2                                                     
                                         WHEN ''20'' THEN 1.5                                                     
                                         WHEN ''30'' THEN 2.0                                                     
                                         ELSE 1.0                                                               
                            END) *                                                                              
                           (CASE type    WHEN ''9.1'' THEN CASE WHEN level1 < level2 THEN  3.0 ELSE  2.0 END      
                                         WHEN ''9.2'' THEN CASE WHEN level1 < level2 THEN 15.0 ELSE 12.0 END      
                                         ELSE 1.0                                                               
                            END) +                                                                              
                           (CASE type    WHEN ''9.3'' THEN 40.0                                                   
                                         ELSE 0.0                                                               
                            END)                                                                                
                 )                                                                                              
        END )::float8 AS reverse_cost, ' ||
        'x1, y1, x2, y2  FROM routing.edges',
         22348, 24635, TRUE, TRUE)