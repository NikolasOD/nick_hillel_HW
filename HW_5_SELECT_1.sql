SELECT TrackId, SUM(UnitPrice) AS 'Total amount' , COUNT(*) AS 'Total quantity'
FROM invoice_items
GROUP BY TrackId;