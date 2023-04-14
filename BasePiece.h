#pragma once
#include <string>

enum class Color {
    Black,
    White
};


typedef struct Coordinates {
    int file;
    int rank;
} Position;


class BasePiece {
    public:
        BasePiece();
        virtual ~BasePiece();

        void printPiece();
        void setPosition(Position pos);
        Position getPosition();
        Color getColor();
        virtual bool isValidMove(Position moveToPosition) = 0;
    protected:
        std::string type;
        Color color;
        Position pos;
};
