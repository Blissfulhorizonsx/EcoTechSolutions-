

create TABLE usuario (
    idUsuario INT AUTO_INCREMENT primary key,
    nombreUsuario VARCHAR(100) NOT NULL UNIQUE,
    contrasenaHash VARCHAR (255) NOT NULL,
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
    numEmple VARCHAR(12),
    mailEmple VARCHAR(100),
    fchContrato DATE,
    salarioCifrado VARCHAR(255),
    idDepart INT,
    FOREIGN KEY (idUsuario) REFERENCES usuario(idUsuario),
    FOREIGN KEY (idDepart) REFERENCES departamento(idDepart)
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
    FOREIGN KEY (idEmple) REFERENCES empleado(idEmple),
    FOREIGN KEY (idProyecto) REFERENCES proyecto(idProyecto)
);

create TABLE asignacion (
    idAsign INT AUTO_INCREMENT PRIMARY KEY,
    fechaAsignacion DATE,
    idEmple INT NOT NULL,
    idProyecto INT NOT NULL,
    UNIQUE (idEmple, idProyecto),
    FOREIGN KEY (idEmple) REFERENCES empleado(idEmple),
    FOREIGN KEY (idProyecto) REFERENCES proyecto(idProyecto)
);

create TABLE informe (
    idInforme INT AUTO_INCREMENT PRIMARY KEY,
    fchGeneracion DATE,
    formato VARCHAR(20),
    contenido TEXT,
    idUsuario INT NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES usuario(idUsuario)
);