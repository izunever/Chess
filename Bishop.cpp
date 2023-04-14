#include "Bishop.h"

Bishop::Bishop(Color color, Position pos) {
    if(color == Color::Black) {
        this->type = "b";
    }
    else {
        this->type = "B";
    }
    this->color=color;
    this->pos = pos;
}

Bishop::~Bishop() {

}

bool Bishop::isValidMove(Position moveToPos) {
    return false;
}
