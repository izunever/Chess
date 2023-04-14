#include "Knight.h"

Knight::Knight(Color color, Position pos) {
    if(color == Color::Black) {
        this->type = "n";
    }
    else {
        this->type = "N";
    }
    this->color=color;
    this->pos = pos;
}

Knight::~Knight() {

}

bool Knight::isValidMove(Position moveToPos) {

    return false;
}