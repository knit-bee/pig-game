class ComputerPlayer:
    aim = 20

    def get_aim(self, scores):
        human_score = scores["human"]
        own_score = scores["computer"]
        diff = abs(human_score - own_score)
        if 100 - own_score <= 25:
            return 100 - own_score

        if own_score >= human_score:
            if diff < 10:
                return self.aim + 2
            else:
                return self.aim - 3
        else:
            if diff > 20:
                return self.aim + min(diff // 3, 13)
            elif diff >= 10:
                return self.aim + 2
            else:
                return self.aim
