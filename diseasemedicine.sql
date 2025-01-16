-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2025 at 10:10 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diseasemedicinedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `diseasemedicine`
--

CREATE TABLE `diseasemedicine` (
  `id` int(11) NOT NULL,
  `disease_name` varchar(255) NOT NULL,
  `medicine_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `diseasemedicine`
--

INSERT INTO `diseasemedicine` (`id`, `disease_name`, `medicine_name`) VALUES
(1, 'Flu', 'Paracetamol'),
(2, 'Flu', 'Ibuprofen'),
(3, 'Diabetes', 'Metformin'),
(4, 'Hypertension', 'Amlodipine'),
(5, 'Hypertension', 'Lisinopril'),
(6, 'Migraine', 'Sumatriptan'),
(7, 'Migraine', 'Ibuprofen');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `diseasemedicine`
--
ALTER TABLE `diseasemedicine`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `diseasemedicine`
--
ALTER TABLE `diseasemedicine`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
