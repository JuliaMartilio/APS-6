CREATE DATABASE  IF NOT EXISTS `controle_acesso` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `controle_acesso`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: controle_acesso
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auditoria`
--

DROP TABLE IF EXISTS `auditoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auditoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_funcionario` int NOT NULL,
  `nome_funcionario` varchar(100) NOT NULL,
  `nivel_acesso` int DEFAULT NULL,
  `id_documento` int NOT NULL,
  `data_acesso` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_funcionario` (`id_funcionario`),
  KEY `id_documento` (`id_documento`),
  CONSTRAINT `auditoria_ibfk_1` FOREIGN KEY (`id_funcionario`) REFERENCES `funcionarios` (`id_funcionario`),
  CONSTRAINT `auditoria_ibfk_2` FOREIGN KEY (`id_documento`) REFERENCES `documentos` (`id_documento`),
  CONSTRAINT `auditoria_chk_1` CHECK ((`nivel_acesso` between 1 and 3))
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auditoria`
--

LOCK TABLES `auditoria` WRITE;
/*!40000 ALTER TABLE `auditoria` DISABLE KEYS */;
INSERT INTO `auditoria` VALUES (21,1,'Geovanna',3,12,'2024-11-15 20:40:40'),(23,1,'Geovanna',3,14,'2024-11-15 20:51:21'),(25,1,'Geovanna',3,16,'2024-11-15 20:56:41'),(26,1,'Geovanna',3,12,'2024-11-15 20:59:01'),(27,1,'Geovanna',3,14,'2024-11-15 20:59:09'),(28,1,'Geovanna',3,16,'2024-11-15 20:59:20'),(30,3,'Julia',2,16,'2024-11-15 21:05:21'),(31,3,'Julia',2,12,'2024-11-15 21:05:26'),(32,4,'Larissa',1,16,'2024-11-15 21:13:22'),(33,4,'Larissa',1,16,'2024-11-17 14:43:11');
/*!40000 ALTER TABLE `auditoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documentos`
--

DROP TABLE IF EXISTS `documentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentos` (
  `id_documento` int NOT NULL AUTO_INCREMENT,
  `nome_documento` varchar(255) NOT NULL,
  `nivel_minimo_acesso` int DEFAULT NULL,
  `conteudo` longblob,
  PRIMARY KEY (`id_documento`),
  CONSTRAINT `documentos_chk_1` CHECK ((`nivel_minimo_acesso` between 1 and 3))
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentos`
--

LOCK TABLES `documentos` WRITE;
/*!40000 ALTER TABLE `documentos` DISABLE KEYS */;
INSERT INTO `documentos` VALUES (12,'Polícia Federal investiga esquema de importação e comercialização ilegal de agrotóxicos',2,_binary 'Policia Federal investiga esquema de importacao e comercializacao ilegal de agrotoxicos.\r\n\r\nSegundo dados do portal G1 Campinas e Regiao (G1 Globo), em 30 de outubro de 2024, foram emitidos dois mandados de busca e apreensao como parte da operacao Terra Limpa. Os alvos foram a residencias pertencentes a empresa do investigado, responsavel pela fabricacao de fertilizantes agricolas usados por produtores agroecologicos. \r\nA investigacao teve inicio em junho, apos a apreensao de uma grande quantidade de rotenona (um agrotoxico importado irregularmente) no Aeroporto Internacional de Viracopos. A substancia nao possuia licenca ou autorizacao dos orgaos de controle e estava com informacoes falsas sobre sua origem. \r\nDurante as investigacoes, foi descoberto que a empresa suspeita havia realizado ao menos 11 importacoes semelhantes.\r\nSegundo o da chefe Policia Federal, a rotenona pode ser importada para fins de fertilizantes e controle de pragas, mas exige autorizacao para controlar a quantidade, destino e os responsaveis pela importacao.\r\nA PF tambem realizara uma fiscalizacao detalhada dos produtos e insumos usados na fabricacao de fertilizantes na empresa investigada, com o objetivo de verificar o uso irregular de agrotoxicos em mercadorias comercializadas para os consumidores.\r\n\r\n'),(14,'Agrotóxicos proibidos são comercializados devido falhas nas regras de importação',3,_binary 'Agrotoxicos proibidos sao comercializados devido falhas nas regras de importacao\r\n\r\nEm 27 de setembro, foi publicado um artigo de nome Brechas na exportacao na Franca permitem remessas crescentes de agrotoxicos banidos na plataforma Blog do Pedlowski, apontando que empresas multinacionais estao exportando grandes quantidades de produtos quimicos proibidos para a producao de pesticidas no exterior. \r\nUma investigacao no exterior revelou como a industria de pesticidas tem explorado a falha de diversos governos em fechar brechas na historica proibicao da exportacao de agrotoxicos proibidos.\r\nEm 2023, algumas autoridades autorizaram a exportacao de mais de 4.500 toneladas de produtos quimicos proibidos nao diluidos para fabricacao de pesticidas, um numero bem superior ao de 3.400 toneladas em 2022. \r\nDois tercos dessas exportacoes tiveram como destino o Brasil, ja que o pais tem algumas das maiores reservas de biodiversidade do planeta. Entre as substancias exportadas estavam a picoxistrobina, um agrotoxico proibido na Europa por suas ameacas a vida selvagem e ao DNA humano, e o fipronil, um inseticida associado ao envenenamento de milhares de colmeias de abelhas no Brasil.\r\nCom isso, as fabricas continuam a exportar essas substancias em sua forma nao diluida, para serem misturadas e transformadas em produtos utilizados no exterior, especialmente no Sul Global.\r\nO Brasil se tornou o maior mercado para os pesticidas mais perigosos, devido ao seu agronegocio em grande escala. Autoridades brasileiras documentaram diversos casos de envenenamento de abelhas causados pelo fipronil. \r\nEm resposta, o IBAMA suspendeu temporariamente a pulverizacao aerea desse inseticida enquanto reavalia o impacto ambiental no pais. No entanto, os agricultores ainda podem usar o fipronil em sementes, aplicar diretamente no solo e pulverizar de forma direcionada nas areas com pragas.\r\n'),(16,'Glifosato Como evitá-lo com a agroecologia',1,_binary 'Glifosato Como evita-lo com a agroecologia\r\n\r\nNa agricultura moderna existe um grande uso de componentes quimicos, normalmente usados para o controle de plantas indesejadas e ate certas pragas, esses sao popularmente conhecidos como agrotoxicos, que acabam sendo prejudiciais a saude humana e para as proprias plantacoes tambem.\r\nEntre os agrotoxicos mais comuns esta o glifosato, comumente utilizado para eliminar plantas indesejadas, por exemplo, ervas daninhas e gramineas. No entanto, o contato com a pele pode permitir sua absorcao, e sua entrada na corrente sanguinea, causando serios problemas de saude, conforme citado pelo site Editora Conceitos em Conceitos de Agrotoxicos.\r\nComo exemplo desses problemas para a saude humana podemos citar malformacoes geneticas, doencas respiratorias, problemas dermatologicos, alergias e ate cancer. Esses efeitos podem evoluir para doencas cronicas ou problemas reprodutivos.\r\nA Organização Mundial da Saude (OMS) confirmou os impactos negativos dos agrotoxicos, recomendando medidas para estabelecer um controle mais rigoroso sobre o uso dessas substancias.\r\nO uso de agrotoxicos e um problema evitavel, pois existem alternativas viaveis que nao causam danos ao meio ambiente ou a saude. A adocao de praticas agroecologicas pode proteger as plantacoes sem recorrer a esses produtos quimicos, inspirada no movimento ambientalista da decada de 1970.\r\nOs agricultores podem seguir as diretrizes da agroecologia, utilizando fertilizantes organicos, reduzindo o uso de maquinario pesado e instalando cercas vivas para demarcar os terrenos.\r\nA agroecologia tem como principio fundamental manter as plantacoes com o menor impacto ambiental possivel, promovendo a sustentabilidade no meio rural. Para atingir esse objetivo, sao necessarias duas estrategias principais: evitar o uso de agrotoxicos e a manipulacao genetica das plantas.');
/*!40000 ALTER TABLE `documentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id_funcionario` int NOT NULL AUTO_INCREMENT,
  `nome_funcionario` varchar(100) NOT NULL,
  `nivel_acesso` int DEFAULT NULL,
  PRIMARY KEY (`id_funcionario`),
  CONSTRAINT `funcionarios_chk_1` CHECK ((`nivel_acesso` between 1 and 3))
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'Geovana',3),(2,'Guilherme',2),(3,'Julia',2),(4,'Larissa',1),(5,'Caio',1);
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-20 14:16:17
