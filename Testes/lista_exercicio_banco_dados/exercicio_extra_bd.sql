CREATE DATABASE exercicio_extra;

CREATE TABLE Aluno (
	id_matricula int,
	nome char(100) not null,
	CONSTRAINT PK_Aluno PRIMARY KEY (id_matricula)
);


CREATE TABLE Disciplina (
	id_disciplina int,
	descricao char(500), 
	CONSTRAINT PK_Disciplina PRIMARY KEY (id_disciplina)
);

CREATE TABLE DISCIPLINA_ALUNO(
	cod_matricula int,
	cod_disciplina int,
	CONSTRAINT FK_Aluno_Id_Matricula FOREIGN KEY(cod_matricula) REFERENCES Aluno(id_matricula),
	CONSTRAINT FK_Disciplina_Id_Disciplina FOREIGN KEY(cod_disciplina) REFERENCES Disciplina(id_disciplina),
	CONSTRAINT PK_Disciplina_Aluno PRIMARY KEY (cod_matricula, cod_disciplina)
);