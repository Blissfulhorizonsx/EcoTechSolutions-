create TABLE usuario (
    idUsuario INT AUTO_INCREMENT primary key,
    nombreUsuario VARCHAR(100) NOT NULL UNIQUE,
    contrasenaHash VARCHAR(255) NOT NULL,
    rol VARCHAR(20) NOT NULL DEFAULT 'EMPLEADO'
);

create TABLE departamento (
    idDepart INT AUTO_INCREMENT primary key,
    nombDepart VARCHAR(100) NOT NULL,
    gerentDepart VARCHAR(100)
);

create TABLE empleado (
    idEmple INT AUTO_INCREMENT PRIMARY KEY,
    idUsuario INT UNIQUE,
    nombEmplea VARCHAR(100) NOT NULL,
    direccEmple VARCHAR(200),
    numEmple VARCHAR(255),
    mailEmple VARCHAR(255),
    fchContrato DATE,
    salarioCifrado VARCHAR(255),
    idDepart INT,
    FOREIGN KEY (idUsuario) REFERENCES usuario (idUsuario),
    FOREIGN KEY (idDepart) REFERENCES departamento (idDepart)
);

create TABLE proyecto (
    idProyecto INT AUTO_INCREMENT PRIMARY KEY,
    nombProyecto VARCHAR(100) NOT NULL UNIQUE,
    descripProyecto VARCHAR(200),
    fchInicio DATE
);

create TABLE registroTiempo (
    idRegistro INT AUTO_INCREMENT PRIMARY KEY,
    fchTrabajo DATE,
    horaInicio TIME NOT NULL,
    horaTermino TIME NOT NULL,
    descripTareas VARCHAR(200),
    idEmple INT NOT NULL,
    idProyecto INT NOT NULL,
    FOREIGN KEY (idEmple) REFERENCES empleado (idEmple),
    FOREIGN KEY (idProyecto) REFERENCES proyecto (idProyecto)
);

create TABLE asignacion (
    idAsign INT AUTO_INCREMENT PRIMARY KEY,
    fechaAsignacion DATE,
    idEmple INT NOT NULL,
    idProyecto INT NOT NULL,
    UNIQUE (idEmple, idProyecto),
    FOREIGN KEY (idEmple) REFERENCES empleado (idEmple),
    FOREIGN KEY (idProyecto) REFERENCES proyecto (idProyecto)
);

create TABLE informe (
    idInforme INT AUTO_INCREMENT PRIMARY KEY,
    fchGeneracion DATE,
    formato VARCHAR(20),
    contenido TEXT,
    idUsuario INT NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES usuario (idUsuario)
);

# PARA LA TABLA INDICADORES LE PEDIMOS A LA INTELIGENCIA ARTIFICAL QUE ERA LO MAS RECOMENDABLE GUARDAR
# O QUE DATOS SE SUELEN GUARDAR EN INDICADORES DE MONEDA CUANDO SE OCUPAN EN PROGRAMAS A TRAVES DE LAS API
# Y ESTA FUE LA TABLA QUE NOS DIO QUE NOS SIRVIO PARA REALIZAR LAS FUNCIONES Y SABER QUE DEBIAMOS GUARDAR EN LA BASE DE DATOS

CREATE TABLE indicadores (
    idIndicador INT AUTO_INCREMENT PRIMARY KEY,
    idUsuario INT NOT NULL,
    autor VARCHAR(30) NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    fecha DATE NOT NULL,
    valor DECIMAL(14, 4) NOT NULL,
    fchConsulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE (codigo, fecha),
    FOREIGN KEY (idUsuario) REFERENCES usuario (idUsuario)
);

CREATE TABLE IF NOT EXISTS recuperacion_clave (
    idRecuperacion INT AUTO_INCREMENT PRIMARY KEY,
    idUsuario INT NOT NULL,
    codigoHash VARCHAR(100) NOT NULL,
    expira DATETIME NOT NULL,
    usado TINYINT(1) NOT NULL DEFAULT 0,
    intentos INT NOT NULL DEFAULT 0,
    creado DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (idUsuario) REFERENCES usuario (idUsuario) ON DELETE CASCADE
);