CREATE TABLE IF NOT EXISTS autor (
    id_AUTOR      SERIAL PRIMARY KEY,
    nome          VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)  NOT NULL
);

CREATE TABLE IF NOT EXISTS livro (
    id_LIVRO        SERIAL PRIMARY KEY,
    titulo          VARCHAR(150) NOT NULL,
    ano_publicacao  INTEGER NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES autor(id_AUTOR) ON DELETE CASCADE
);
