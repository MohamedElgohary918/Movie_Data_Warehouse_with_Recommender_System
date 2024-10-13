CREATE TABLE [dbo].[Movies] (
  [Movie_id] [int] NOT NULL,
  [movie_name] [varchar](255) NULL,
  [imdb_id] [varchar](255) NULL,
  [year] [int] NULL,
  PRIMARY KEY CLUSTERED ([Movie_id])
)
ON [PRIMARY]
GO