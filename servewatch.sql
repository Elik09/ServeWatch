-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 11, 2022 at 09:17 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `servewatch`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('0033ef6d348f');

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `id` int(11) NOT NULL,
  `log_id` varchar(200) NOT NULL,
  `machine` varchar(100) NOT NULL,
  `action` varchar(100) NOT NULL,
  `file_path` varchar(500) DEFAULT NULL,
  `modified` datetime NOT NULL,
  `date_posted` datetime NOT NULL,
  `user` varchar(200) NOT NULL,
  `ip` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`id`, `log_id`, `machine`, `action`, `file_path`, `modified`, `date_posted`, `user`, `ip`) VALUES
(4, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Created', '/tmp/x', '2022-03-22 12:04:16', '2022-03-22 09:04:16', 'root', '127.0.0.1'),
(5, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Modified', '/tmp/x', '2022-03-22 12:04:16', '2022-03-22 09:04:16', 'root', '127.0.0.1'),
(6, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Modified', '/tmp/.com.google.Chrome.mwIpRp', '2022-03-22 12:04:59', '2022-03-22 09:04:59', 'root', '127.0.0.1'),
(7, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Created', '/tmp/x', '2022-03-23 20:42:34', '2022-03-23 17:42:34', 'root', '127.0.0.1'),
(8, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Modified', '/tmp/x', '2022-03-23 20:42:34', '2022-03-23 17:42:34', 'root', '127.0.0.1'),
(9, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Created', '/tmp/server-0.xkm', '2022-03-23 20:54:17', '2022-03-23 17:54:17', 'root', '127.0.0.1'),
(10, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Modified', '/tmp/server-0.xkm', '2022-03-23 20:54:17', '2022-03-23 17:54:17', 'root', '127.0.0.1'),
(11, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Deleted', '/tmp/server-0.xkm', '2022-03-23 20:54:17', '2022-03-23 17:54:17', 'root', '127.0.0.1'),
(12, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Created', '/tmp/.com.google.Chrome.Ez7vXi', '2022-03-23 21:02:26', '2022-03-23 18:02:26', 'root', '127.0.0.1'),
(13, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Modified', '/tmp/.com.google.Chrome.Ez7vXi', '2022-03-23 21:02:26', '2022-03-23 18:02:26', 'root', '127.0.0.1'),
(14, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Deleted', '/tmp/.com.google.Chrome.Ez7vXi', '2022-03-23 21:02:26', '2022-03-23 18:02:26', 'root', '127.0.0.1'),
(15, '6437c9f7785ccb1b688faae3f47429af', 'MacBook-Pro', 'File_Modified', '/tmp/.com.google.Chrome.Ez7vXi', '2022-03-23 21:02:34', '2022-03-23 18:02:34', 'root', '127.0.0.1');

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `permissions` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `default`, `permissions`) VALUES
(1, 'viewer', 1, 96),
(2, 'admin', 0, 255);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `email` varchar(120) NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `image_file` varchar(100) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password_hash`, `email`, `status`, `created_at`, `last_login`, `ip`, `image_file`, `role_id`) VALUES
(2, 'test', 'pbkdf2:sha256:150000$ocjTaHAT$2c4c873e7481307b26ce437891728fcb7728dcfa3c5792b288b9fb5edba6ac89', 'test@gmail.com', 'active', '2022-03-17 08:45:03', '2022-03-17 08:45:03', '127.0.0.1', 'default.jpg', 1),
(3, 'admin', 'pbkdf2:sha256:150000$y9Reblic$655edcea827cbdba16bb08fcf28a99d276ae05ab5424db90940be6d85f01384d', 'admin@gmail.com', 'active', '2022-03-17 08:45:03', '2022-03-17 08:45:03', '127.0.0.1', 'default.jpg', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_roles_default` (`default`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
