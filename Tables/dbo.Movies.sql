CREATE TABLE [dbo].[Movies] (
  [movie_id] [int] NOT NULL,
  [movie_name] [varchar](255) NULL,
  [release_year] [int] NULL,
  [imdb_id] [varchar](255) NULL,
  PRIMARY KEY CLUSTERED ([movie_id])
)
ON [PRIMARY]
GO