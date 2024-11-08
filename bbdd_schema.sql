-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS InventarioEquipos;
USE InventarioEquipos;

-- Creación de la tabla Clientes
CREATE TABLE Clientes (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL
);

-- Creación de la tabla Contactos
CREATE TABLE Contactos (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(50),
    CorreoElectronico VARCHAR(100),
    Telefono VARCHAR(15)
);

-- Creación de la tabla Sitios
CREATE TABLE Sitios (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    ClienteId INT,
    Ubicacion VARCHAR(200),
    FOREIGN KEY (ClienteId) REFERENCES Clientes(Id)
);

-- Creación de la tabla de relación ContactosSitios para manejar la relación muchos-a-muchos entre Contactos y Sitios
CREATE TABLE ContactosSitios (
    SitioId INT,
    ContactoId INT,
    PRIMARY KEY (SitioId, ContactoId),
    FOREIGN KEY (SitioId) REFERENCES Sitios(Id) ON DELETE CASCADE,
    FOREIGN KEY (ContactoId) REFERENCES Contactos(Id) ON DELETE CASCADE
);

-- Creación de la tabla Equipos
CREATE TABLE Equipos (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Proveedor VARCHAR(100),
    Marca VARCHAR(50),
    Nserie VARCHAR(50) UNIQUE,
    Licencia VARCHAR(100),
    FechaCompra DATE,
    EstaEnSoporte BOOLEAN DEFAULT TRUE,
    SitioId INT,
    FechaFin DATE,
    Renovacion DATE,
    ContactoId INT,
    FOREIGN KEY (SitioId) REFERENCES Sitios(Id),
    FOREIGN KEY (ContactoId) REFERENCES Contactos(Id)
);

-- Actualización en la tabla Clientes para relacionar PersonaContactoId con Contactos
ALTER TABLE Clientes
ADD PersonaContactoId INT,
ADD FOREIGN KEY (PersonaContactoId) REFERENCES Contactos(Id);
