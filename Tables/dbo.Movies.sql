CREATE TABLE [dbo].[Movies] (
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
GO