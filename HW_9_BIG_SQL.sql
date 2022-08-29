  SELECT alb.Title AS 'Album name',
	     g.Name AS 'Genre',
	     t.Composer AS 'Artist or Group',
	     ROUND(SUM(t.Milliseconds)/60000) AS 'Duration (Minuts)',
	     ROUND(SUM(t.Bytes)/1048576) AS 'Size (Mb)',
	     SUM(t.UnitPrice) AS 'Album price',
	     COUNT(t.TrackId) AS 'Count tracks'
    FROM tracks AS t
	JOIN albums AS alb ON t.AlbumId = alb.AlbumId
	JOIN genres AS g ON t.GenreId = g.GenreId
	JOIN media_types AS mt ON t.MediaTypeId = mt.MediaTypeId
   WHERE mt.Name = 'MPEG audio file'
   GROUP BY alb.Title
   ORDER BY g.Name, t.Composer;