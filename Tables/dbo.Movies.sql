<<<<<<< HEAD
﻿CREATE TABLE [dbo].[Movies] (
  [movie_id] [int] IDENTITY,
  [movie_name] [varchar](255) NULL,
  [overview] [text] NULL,
  [duration] [float] NULL,
  [release_date] [date] NULL,
  [release_country] [varchar](255) NULL,
  PRIMARY KEY CLUSTERED ([movie_id])
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
=======
﻿CREATE TABLE [dbo].[Movies] (
  [movie_id] [int] NOT NULL,
  [movie_name] [varchar](255) NULL,
  [release_year] [int] NULL,
  [imdb_id] [varchar](255) NULL,
  PRIMARY KEY CLUSTERED ([movie_id])
)
ON [PRIMARY]
>>>>>>> 30466eeeb1dd94f3f9470b34a955a5f96a512944
GO