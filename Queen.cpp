#include "Queen.h"


Queen::Queen(Color color, Position pos) {
    if(color == Color::Black) {
        this->type = "q";
    }
    else {
        this->type = "Q";
    }
    this->color=color;
    this->pos = pos;
}

Queen::~Queen() {

}

bool Queen::isValidMove(Position moveToPos) {

    return false;
}