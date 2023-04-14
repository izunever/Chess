#include "King.h"

King::King(Color color, Position pos) {
   if(color == Color::Black) {
        this->type = "k";
    }
    else {
        this->type = "K";
    }
    this->color=color;
    this->pos = pos;
}

King::~King() {

}

bool King::isValidMove(Position moveToPos) {

    return false;
}