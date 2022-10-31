DROP DATABASE NIRVANA;
CREATE DATABASE NIRVANA;
USE NIRVANA;

CREATE TABLE NirvanaUsers (
  username VARCHAR(50) NOT NULL,
  password VARCHAR(100) NOT NULL,
  enabled TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (username)
);

CREATE TABLE authorities (
  username VARCHAR(50) NOT NULL,
  authority VARCHAR(50) NOT NULL,
  FOREIGN KEY (username) REFERENCES users(username)
);

CREATE UNIQUE INDEX ix_auth_username
  on authorities (username,authority);

--
-- Create model Album
--
CREATE TABLE `Album` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `album_title` varchar(50) NOT NULL, `album_logo` varchar(100) NOT NULL);
--
-- Create model Artist
--
CREATE TABLE `Artist` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `username` varchar(255) NOT NULL, `email` varchar(254) NOT NULL UNIQUE, `is_active` bool NOT NULL, `is_staff` bool NOT NULL, `created_at` datetime(6) NOT NULL, `updated_at` datetime(6) NOT NULL, `password` varchar(30) NOT NULL, `about` longtext NOT NULL, `twitter` varchar(200) NOT NULL, `facebook` varchar(200) NOT NULL, `instagram` varchar(200) NOT NULL);
--
-- Create model Country
--
CREATE TABLE `Country` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(30) NOT NULL UNIQUE);
--
-- Create model Genre
--
CREATE TABLE `Genre` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(50) NOT NULL UNIQUE);
--
-- Create model Playlist
--
CREATE TABLE `Playlist` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(50) NOT NULL, `description` longtext NOT NULL, `type` varcharvisibilityAlbumReleaseInfo(4) NOT NULL, `visibility` varchar(4) NOT NULL, `created_by_artist_id` bigint NULL);
--
-- Create model RecordLabel
--
CREATE TABLE `RecordLabel` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `username` varchar(255) NOT NULL, `email` varchar(254) NOT NULL UNIQUE, `password` varchar(50) NOT NULL, `is_active` bool NOT NULL, `is_staff` bool NOT NULL, `created_at` datetime(6) NOT NULL, `updated_at` datetime(6) NOT NULL, `name` varchar(50) NOT NULL, `description` varchar(5000) NOT NULL, `record_label_logo` varchar(100) NOT NULL, `twitter` varchar(200) NOT NULL, `facebook` varchar(200) NOT NULL, `instagram` varchar(200) NOT NULL);
--
-- Create model Track
--
CREATE TABLE `Track` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(250) NOT NULL, `audio_file` varchar(100) NOT NULL, `track_length` bigint NOT NULL, `explicit_content` bool NOT NULL, `writer` varchar(50) NOT NULL, `composer` varchar(50) NOT NULL, `producer` varchar(50) NOT NULL, `lyrics` longtext NOT NULL, `album_id` bigint NOT NULL);
--
-- Create model User
--
CREATE TABLE `allmodels_user` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `username` varchar(255) NOT NULL, `email` varchar(254) NOT NULL UNIQUE, `password` varchar(30) NOT NULL, `is_active` bool NOT NULL, `is_staff` bool NOT NULL, `created_at` datetime(6) NOT NULL, `updated_at` datetime(6) NOT NULL, `nationality_id` bigint NOT NULL);
--
-- Create model TrackLikes
--
CREATE TABLE `TrackLikes` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `liked_by_id` bigint NOT NULL, `track_id` bigint NOT NULL);
--
-- Add field liked_by to track
--
-- (no-op)
--
-- Create model PlaylistParticipants
--
CREATE TABLE `PlaylistParticipation` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `participant_id` bigint NOT NULL, `playlist_id` bigint NOT NULL);
--
-- Create model PlaylistLikes
--
CREATE TABLE `PlaylistLikes` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `liked_by_id` bigint NOT NULL, `playlist_id` bigint NOT NULL);
--
-- Create model PlaylistContent
--
CREATE TABLE `PlaylistContent` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `added_by_id` bigint NULL, `playlist_id` bigint NOT NULL, `track_id` bigint NOT NULL);
--
-- Add field created_by_user to playlist
--
ALTER TABLE `Playlist` ADD COLUMN `created_by_user_id` bigint NULL , ADD CONSTRAINT `Playlist_created_by_user_id_fb2a2c4c_fk_allmodels_user_id` FOREIGN KEY (`created_by_user_id`) REFERENCES `allmodels_user`(`id`);
--

-- Create model History
--
CREATE TABLE `History` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `time` datetime(6) NOT NULL, `track_id` bigint NOT NULL, `user_id` bigint NOT NULL);
--
-- Create model Event
--
CREATE TABLE `Event` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `time` time(6) NOT NULL, `venue` longtext NOT NULL, `registration` varchar(200) NOT NULL, `event_poster` varchar(100) NOT NULL, `artist_id` bigint NOT NULL, `country_id` bigint NOT NULL);
--
-- Create model ArtistPhotos
--
CREATE TABLE `ArtistPhotos` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `photo` varchar(100) NOT NULL, `date_added` date NOT NULL, `artist_id` bigint NOT NULL);
--
-- Add field nationality to artist
--
ALTER TABLE `Artist` ADD COLUMN `nationality_id` bigint NOT NULL , ADD CONSTRAINT `Artist_nationality_id_daa9421c_fk_Country_id` FOREIGN KEY (`nationality_id`) REFERENCES `Country`(`id`);
--
-- Add field record_label to artist
--
ALTER TABLE `Artist` ADD COLUMN `record_label_id` bigint NOT NULL , ADD CONSTRAINT `Artist_record_label_id_d5f7ba7d_fk_RecordLabel_id` FOREIGN KEY (`record_label_id`) REFERENCES `RecordLabel`(`id`);
--
-- Create model AlbumLikes
--
CREATE TABLE `AlbumLikes` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `album_id` bigint NOT NULL, `liked_by_id` bigint NOT NULL);
--
-- Add field artist to album
--
ALTER TABLE `Album` ADD COLUMN `artist_id` bigint NOT NULL , ADD CONSTRAINT `Album_artist_id_2fae31c8_fk_Artist_id` FOREIGN KEY (`artist_id`) REFERENCES `Artist`(`id`);
--
-- Add field genre to album
--
ALTER TABLE `Album` ADD COLUMN `genre_id` bigint NOT NULL , ADD CONSTRAINT `Album_genre_id_f15df300_fk_Genre_id` FOREIGN KEY (`genre_id`) REFERENCES `Genre`(`id`);
--
-- Add field liked_by to album
--
-- Create model LikedSong
--
CREATE TABLE `LikedSong` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `time` datetime(6) NOT NULL, `track_id` bigint NOT NULL, `user_id` bigint NOT NULL);
--
-- Create model Followers
--
CREATE TABLE `Followers` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `artist_id` bigint NOT NULL, `followed_by_id` bigint NOT NULL);
--
-- Create model AlbumReleaseInfo
--
CREATE TABLE `AlbumReleaseInfo` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `album_id` bigint NOT NULL, `country_id` bigint NOT NULL);
CREATE INDEX `Artist_username_8bf646df` ON `Artist` (`username`);
ALTER TABLE `Playlist` ADD CONSTRAINT `Playlist_created_by_artist_id_7653970c_fk_Artist_id` FOREIGN KEY (`created_by_artist_id`) REFERENCES `Artist` (`id`);
CREATE INDEX `RecordLabel_username_785e9807` ON `RecordLabel` (`username`);
ALTER TABLE `Track` ADD CONSTRAINT `Track_album_id_5410aa80_fk_Album_id` FOREIGN KEY (`album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `allmodels_user` ADD CONSTRAINT `allmodels_user_nationality_id_c487603f_fk_Country_id` FOREIGN KEY (`nationality_id`) REFERENCES `Country` (`id`);
CREATE INDEX `allmodels_user_username_f3b023a1` ON `allmodels_user` (`username`);
ALTER TABLE `TrackLikes` ADD CONSTRAINT `TrackLikes_track_id_liked_by_id_9f84bc69_uniq` UNIQUE (`track_id`, `liked_by_id`);
ALTER TABLE `TrackLikes` ADD CONSTRAINT `TrackLikes_liked_by_id_6e5ee846_fk_allmodels_user_id` FOREIGN KEY (`liked_by_id`) REFERENCES `allmodels_user` (`id`);
ALTER TABLE `TrackLikes` ADD CONSTRAINT `TrackLikes_track_id_2bab2d5d_fk_Track_id` FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `PlaylistParticipation` ADD CONSTRAINT `PlaylistParticipation_playlist_id_participant_id_c8c60688_uniq` UNIQUE (`playlist_id`, `participant_id`);
ALTER TABLE `PlaylistParticipation` ADD CONSTRAINT `PlaylistParticipatio_participant_id_423b33b7_fk_allmodels` FOREIGN KEY (`participant_id`) REFERENCES `allmodels_user` (`id`);
ALTER TABLE `PlaylistParticipation` ADD CONSTRAINT `PlaylistParticipation_playlist_id_9250fc97_fk_Playlist_id` FOREIGN KEY (`playlist_id`) REFERENCES `Playlist` (`id`);
ALTER TABLE `PlaylistLikes` ADD CONSTRAINT `PlaylistLikes_liked_by_id_50d6ac86_fk_allmodels_user_id` FOREIGN KEY (`liked_by_id`) REFERENCES `allmodels_user` (`id`);
ALTER TABLE `PlaylistLikes` ADD CONSTRAINT `PlaylistLikes_playlist_id_9bb2dd84_fk_Playlist_id` FOREIGN KEY (`playlist_id`) REFERENCES `Playlist` (`id`);
ALTER TABLE `PlaylistContent` ADD CONSTRAINT `PlaylistContent_track_id_added_by_id_b8f2b9b3_uniq` UNIQUE (`track_id`, `added_by_id`);
ALTER TABLE `PlaylistContent` ADD CONSTRAINT `PlaylistContent_added_by_id_9679739f_fk_allmodels_user_id` FOREIGN KEY (`added_by_id`) REFERENCES `allmodels_user` (`id`);
ALTER TABLE `PlaylistContent` ADD CONSTRAINT `PlaylistContent_playlist_id_1c7cdde9_fk_Playlist_id` FOREIGN KEY (`playlist_id`) REFERENCES `Playlist` (`id`);
ALTER TABLE `PlaylistContent` ADD CONSTRAINT `PlaylistContent_track_id_6494e343_fk_Track_id` FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `History` ADD CONSTRAINT `History_track_id_4af38d99_fk_Track_id` FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `History` ADD CONSTRAINT `History_user_id_ea3c25ec_fk_allmodels_user_id` FOREIGN KEY (`user_id`) REFERENCES `allmodels_user` (`id`);
ALTER TABLE `Event` ADD CONSTRAINT `Event_artist_id_4d204601_fk_Artist_id` FOREIGN KEY (`artist_id`) REFERENCES `Artist` (`id`);
ALTER TABLE `Event` ADD CONSTRAINT `Event_country_id_2b307a95_fk_Country_id` FOREIGN KEY (`country_id`) REFERENCES `Country` (`id`);
ALTER TABLE `ArtistPhotos` ADD CONSTRAINT `ArtistPhotos_artist_id_31ac2171_fk_Artist_id` FOREIGN KEY (`artist_id`) REFERENCES `Artist` (`id`);
ALTER TABLE `AlbumLikes` ADD CONSTRAINT `AlbumLikes_album_id_liked_by_id_82c777eb_uniq` UNIQUE (`album_id`, `liked_by_id`);
ALTER TABLE `AlbumLikes` ADD CONSTRAINT `AlbumLikes_album_id_4e40e0d7_fk_Album_id` FOREIGN KEY (`album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `AlbumLikes` ADD CONSTRAINT `AlbumLikes_liked_by_id_7cf3d101_fk_allmodels_user_id` FOREIGN KEY (`liked_by_id`) REFERENCES `allmodels_user` (`id`);
ALTER TABLE `LikedSong` ADD CONSTRAINT `LikedSong_user_id_track_id_992a4e80_uniq` UNIQUE (`user_id`, `track_id`);
ALTER TABLE `LikedSong` ADD CONSTRAINT `LikedSong_track_id_47406299_fk_Track_id` FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `LikedSong` ADD CONSTRAINT `LikedSong_user_id_c6543b63_fk_allmodels_user_id` FOREIGN KEY (`user_id`) REFERENCES `allmodels_user` (`id`);
ALTER TABLE `Followers` ADD CONSTRAINT `Followers_artist_id_followed_by_id_1d4629b8_uniq` UNIQUE (`artist_id`, `followed_by_id`);
ALTER TABLE `Followers` ADD CONSTRAINT `Followers_artist_id_73d2e2c6_fk_Artist_id` FOREIGN KEY (`artist_id`) REFERENCES `Artist` (`id`);
ALTER TABLE `Followers` ADD CONSTRAINT `Followers_followed_by_id_6ee9e054_fk_allmodels_user_id` FOREIGN KEY (`followed_by_id`) REFERENCES `allmodels_user` (`id`);
ALTER TABLE `AlbumReleaseInfo` ADD CONSTRAINT `AlbumReleaseInfo_album_id_country_id_cc174c28_uniq` UNIQUE (`album_id`, `country_id`);
ALTER TABLE `AlbumReleaseInfo` ADD CONSTRAINT `AlbumReleaseInfo_album_id_3c5f4e15_fk_Album_id` FOREIGN KEY (`album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `AlbumReleaseInfo` ADD CONSTRAINT `AlbumReleaseInfo_country_id_f6b3806c_fk_Country_id` FOREIGN KEY (`country_id`) REFERENCES `Country` (`id`);
