# -*- coding:utf-8 -*-

import time


class Elevator(object):
    def __init__(self):
        self.internal_request = [0 for _ in range(20)]
        self.external_request = [0 for _ in range(20)]
        # 1 means running,0 means vacancy
        self.status = 0
        # 1 means up,-1 means down,0 means vacancy
        self.direction = 0
        self.current_floor = 1
        self.destination = 1
        # Used for round-robin schedule
        self.isRotated = 0
        self.rotateDes = 0

    def set_internal(self, f):
        self.internal_request[int(f-1)] = 1

    def set_external(self, f, direction):
        if direction == 1:
            self.external_request[int(f-1)] = 1
        elif direction == -1:
            self.external_request[int(f-1)] = -1

    def update_direction(self):
        if self.destination == self.current_floor:
            self.direction = 0
            self.status = 0
        else:
            self.direction = (self.destination - self.current_floor)/abs(self.destination - self.current_floor)
            self.status = 1

    def update_destination(self, floor):
        if abs(floor - self.current_floor) > abs(self.destination - self.current_floor):
            self.destination = floor

    def check_internal(self, floor):
        i_direction = (floor - self.current_floor)/abs(floor - self.current_floor)
        if i_direction*self.direction < 0:
            return False
        return True

    def check_open(self):
        if self.internal_request[int(self.current_floor - 1)] == 1:
            time.sleep(0.5)
            self.internal_request[int(self.current_floor - 1)] = 0
        if abs(self.external_request[int(self.current_floor - 1)]) == 1:
            time.sleep(0.5)
            self.external_request[int(self.current_floor - 1)] = 0

    def run(self):
        while True:
            self.update_direction()
            if not self.direction == 0:
                self.current_floor += self.direction
                self.check_open()
            elif not self.isRotated == 0:
                self.destination = self.rotateDes
                self.isRotated = 0
            time.sleep(0.5)


class Controller(object):
    def __init__(self):
        self.elevator1 = Elevator()
        self.elevator2 = Elevator()
        self.elevator3 = Elevator()
        self.elevator4 = Elevator()
        self.elevator5 = Elevator()

    # flag:0: internal request,1: external request,ele_num: number of elevator requesting
    # floor: request floor,direction: direction of external request
    def dispatch(self, flag, ele_num, floor, direction):
        # Internal request
        if flag == 0:
            if ele_num == 1:
                if self.elevator1.check_internal(floor):
                    self.elevator1.set_internal(floor)
                    self.elevator1.update_destination(floor)
                else:
                    print("Internal request error!")
            elif ele_num == 2:
                if self.elevator2.check_internal(floor):
                    self.elevator2.set_internal(floor)
                    self.elevator2.update_destination(floor)
                else:
                    print("Internal request error!")
            elif ele_num == 3:
                if self.elevator3.check_internal(floor):
                    self.elevator3.set_internal(floor)
                    self.elevator3.update_destination(floor)
                else:
                    print("Internal request error!")
            elif ele_num == 4:
                if self.elevator4.check_internal(floor):
                    self.elevator4.set_internal(floor)
                    self.elevator4.update_destination(floor)
                else:
                    print("Internal request error!")
            elif ele_num == 5:
                if self.elevator5.check_internal(floor):
                    self.elevator5.set_internal(floor)
                    self.elevator5.update_destination(floor)
                else:
                    print("Internal request error!")
            else:
                raise print("Ele_num error!")
        # External request
        elif flag == 1:
            if not self.find_nearest(floor, direction):
                if not self.find_vacant(floor, direction):
                    self.find_rotate(floor, direction)
        else:
            raise print("Request type error!")

    def find_nearest(self, floor, direction):
        distance = [0 for _ in range(5)]
        # Calculate the distance between each elevator and destination,100 means
        # the elevator is not running closer to destination
        if min(self.elevator1.current_floor, self.elevator1.destination) < floor \
                < max(self.elevator1.current_floor, self.elevator1.destination) and \
                self.elevator1.direction == direction:
            distance[0] = abs(self.elevator1.current_floor - floor)
        else:
            distance[0] = 100

        if min(self.elevator2.current_floor, self.elevator2.destination) < floor \
                < max(self.elevator2.current_floor, self.elevator2.destination) and \
                self.elevator2.direction == direction:
            distance[1] = abs(self.elevator2.current_floor - floor)
        else:
            distance[1] = 100

        if min(self.elevator3.current_floor, self.elevator3.destination) < floor \
                < max(self.elevator3.current_floor, self.elevator3.destination) and \
                self.elevator3.direction == direction:
            distance[2] = abs(self.elevator3.current_floor - floor)
        else:
            distance[2] = 100

        if min(self.elevator4.current_floor, self.elevator4.destination) < floor \
                < max(self.elevator4.current_floor, self.elevator4.destination) and \
                self.elevator4.direction == direction:
            distance[3] = abs(self.elevator4.current_floor - floor)
        else:
            distance[3] = 100

        if min(self.elevator5.current_floor, self.elevator5.destination) < floor \
                < max(self.elevator5.current_floor, self.elevator5.destination) and \
                self.elevator5.direction == direction:
            distance[4] = abs(self.elevator5.current_floor - floor)
        else:
            distance[4] = 100

        min_dis = min(distance)
        if min_dis == 100:
            return False
        else:
            min_index = distance.index(min_dis) + 1
            if min_index == 1:
                self.elevator1.set_external(floor, direction)
            elif min_index == 2:
                self.elevator2.set_external(floor, direction)
            elif min_index == 3:
                self.elevator3.set_external(floor, direction)
            elif min_index == 4:
                self.elevator4.set_external(floor, direction)
            elif min_index == 5:
                self.elevator5.set_external(floor, direction)
            return True

    def find_vacant(self, floor, direction):
        if self.elevator1.status == 0:
            self.elevator1.set_external(floor, direction)
            self.elevator1.status = 1
            self.elevator1.destination = floor
            return True
        elif self.elevator2.status == 0:
            self.elevator2.set_external(floor, direction)
            self.elevator2.status = 1
            self.elevator2.destination = floor
            return True
        elif self.elevator3.status == 0:
            self.elevator3.set_external(floor, direction)
            self.elevator3.status = 1
            self.elevator3.destination = floor
            return True
        elif self.elevator4.status == 0:
            self.elevator4.set_external(floor, direction)
            self.elevator4.status = 1
            self.elevator4.destination = floor
            return True
        elif self.elevator5.status == 0:
            self.elevator5.set_external(floor, direction)
            self.elevator5.status = 1
            self.elevator5.destination = floor
            return True
        else:
            return False

    def find_rotate(self, floor, direction):
        if self.elevator1.isRotated == 0:
            self.elevator1.isRotated = 1
            self.elevator1.rotateDes = floor
            self.elevator1.external_request[int(floor - 1)] = direction
        elif self.elevator2.isRotated == 0:
            self.elevator2.isRotated = 1
            self.elevator2.rotateDes = floor
            self.elevator2.external_request[int(floor - 1)] = direction
        elif self.elevator3.isRotated == 0:
            self.elevator3.isRotated = 1
            self.elevator3.rotateDes = floor
            self.elevator3.external_request[int(floor - 1)] = direction
        elif self.elevator4.isRotated == 0:
            self.elevator4.isRotated = 1
            self.elevator4.rotateDes = floor
            self.elevator4.external_request[int(floor - 1)] = direction
        elif self.elevator5.isRotated == 0:
            self.elevator5.isRotated = 1
            self.elevator5.rotateDes = floor
            self.elevator5.external_request[int(floor - 1)] = direction
        else:
            print("Can't respond this request!")