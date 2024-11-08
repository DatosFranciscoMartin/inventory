-- Inserción de datos en la tabla Clientes
INSERT INTO Clientes (Nombre) VALUES
('Cliente A'),
('Cliente B'),
('Cliente C');

-- Inserción de datos en la tabla Contactos
INSERT INTO Contactos (Nombre, Apellidos, CorreoElectronico, Telefono) VALUES
('Juan', 'Perez', 'juan.perez@example.com', '555-1234'),
('Maria', 'Lopez', 'maria.lopez@example.com', '555-5678'),
('Carlos', 'Martinez', 'carlos.martinez@example.com', '555-8765'),
('Ana', 'Garcia', 'ana.garcia@example.com', '555-4321');

-- Actualización de la tabla Clientes para asociar un contacto principal (PersonaContactoId)
UPDATE Clientes SET PersonaContactoId = 1 WHERE Id = 1; -- Juan para Cliente A
UPDATE Clientes SET PersonaContactoId = 2 WHERE Id = 2; -- Maria para Cliente B
UPDATE Clientes SET PersonaContactoId = 3 WHERE Id = 3; -- Carlos para Cliente C

-- Inserción de datos en la tabla Sitios
INSERT INTO Sitios (Nombre, ClienteId, Ubicacion) VALUES
('Sitio 1', 1, '123 Calle Principal'),
('Sitio 2', 1, '456 Avenida Secundaria'),
('Sitio 3', 2, '789 Calle Tercera');

-- Inserción de datos en la tabla de relación ContactosSitios
INSERT INTO ContactosSitios (SitioId, ContactoId) VALUES
(1, 1), -- Juan asociado a Sitio 1
(1, 2), -- Maria asociado a Sitio 1
(2, 2), -- Maria asociado a Sitio 2
(2, 3), -- Carlos asociado a Sitio 2
(3, 4); -- Ana asociado a Sitio 3

-- Inserción de datos en la tabla Equipos
INSERT INTO Equipos (Proveedor, Marca, Nserie, Licencia, FechaCompra, EstaEnSoporte, SitioId, FechaFin, Renovacion, ContactoId) VALUES
('Proveedor 1', 'Marca A', 'SN12345', 'Licencia A', '2022-01-15', TRUE, 1, '2023-01-15', '2023-12-15', 1),
('Proveedor 2', 'Marca B', 'SN67890', 'Licencia B', '2022-05-20', TRUE, 1, '2023-05-20', '2024-05-20', 2),
('Proveedor 3', 'Marca C', 'SN54321', 'Licencia C', '2021-09-10', FALSE, 2, '2022-09-10', '2023-09-10', 3),
('Proveedor 1', 'Marca A', 'SN09876', 'Licencia D', '2023-03-25', TRUE, 3, '2024-03-25', '2025-03-25', 4);
