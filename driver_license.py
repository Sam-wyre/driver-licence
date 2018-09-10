class exam_check(object):
    def __init__(self):
        self.no_corect_ans = []
        self.incorrect_ans = []
        self.index_incorrect_ans = []
        self.index_correct_ans = []
        self.correct_answers = ['A',
                                'C',
                                'A',
                                'A',
                                'D',
                                'B',
                                'C',
                                'A',
                                'C',
                                'B',
                                'A',
                                'D',
                                'C',
                                'A',
                                'D',
                                'C',
                                'B',
                                'B',
                                'D',
                                'A']
        self.candidate_ans = []
        print("Result is processing")

    def read_answer(self, filepath):
        for line in open(filepath,'r').readlines():
            self.candidate_ans.append(line.strip().upper())

    def check(self):
        print (' '.join(map(str, self.candidate_ans)))
        for i in range(self.correct_answers.__len__()):
            if self.correct_answers[i] == self.candidate_ans[i]:
                self.no_corect_ans.append(self.candidate_ans[i])
                self.index_correct_ans.append(i+1)
            else:
                self.incorrect_ans.append(self.candidate_ans[i])
                self.index_incorrect_ans.append(i+1)

    def result_display(self):
        if (self.no_corect_ans.__len__() >= 15):
            print ("Candidate Passed")
        else:
            print ("Candidate Failed")
        print ("Number of Correct answers was " + str(self.no_corect_ans.__len__()))
        print ("Number of Incorrect answers was " + str(self.incorrect_ans.__len__()))
        print ("Questions number of incorrectly answered questions are "+ ' '.join(map(str, self.index_incorrect_ans)))

ex = exam_check()
ex.read_answer('C:\\Users\\User\\PycharmProjects\\hackerrank\\res')
ex.check()
ex.result_display()