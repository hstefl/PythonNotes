"""
https://edube.org/learn/pcpp1-5/lab-csv-lab-2
"""
import csv
from typing import Generator


class ExamResult:
    def __init__(self, exam_name, candidate_id, score, grade):
        self.exam_name = exam_name
        self.candidate_id = candidate_id
        self.score = score
        self.grade = grade


class ExamReader:
    def __init__(self, exam_file='exam_results.csv'):
        self.exam_file = exam_file

    def get_exam_result(self) -> Generator:
        with open(self.exam_file, newline='') as exams:
            exams_ = csv.DictReader(exams, delimiter=',')
            for exam_ in exams_:
                yield ExamResult(exam_['Exam Name'], exam_['Candidate ID'], int(exam_['Score']), exam_['Grade'])


class ExamReportCreator:
    class ReportLine:
        def __init__(self, candidates_number=0, passed=0, failed=0, best_score=0, worst_score=10000):
            self.candidates_number = candidates_number
            self.passed = passed
            self.failed = failed
            self.best_score = best_score
            self.worst_score = worst_score

    class Report:
        def __init__(self):
            self.data: dict[str, ExamReportCreator.ReportLine] = dict()

        def __iadd__(self, other):
            if isinstance(other, ExamResult):
                if other.exam_name not in self.data:
                    self.data[other.exam_name] = ExamReportCreator.ReportLine()

                self.data[other.exam_name].candidates_number += 1
                if other.grade == "Pass":
                    self.data[other.exam_name].passed += 1
                else:
                    self.data[other.exam_name].failed += 1
                if other.score > self.data[other.exam_name].best_score:
                    self.data[other.exam_name].best_score = other.score
                if other.score < self.data[other.exam_name].worst_score:
                    self.data[other.exam_name].worst_score = other.score

                return self

            else:
                raise TypeError('Unsupported type, ExamResult expected')

        def get_rows(self):
            for exam_name, stats in self.data.items():
                yield [
                    exam_name, stats.candidates_number, stats.passed, stats.failed, stats.best_score,
                    stats.worst_score
                ]

    def __init__(self, filename_='exam_report.csv', exam_reader=None):
        self.report: ExamReportCreator.Report = ExamReportCreator.Report()
        self.filename = filename_
        self.exam_reader = exam_reader if exam_reader is not None else ExamReader()

    def _load_results(self):
        for exam_result in self.exam_reader.get_exam_result():
            self.report += exam_result

    def create(self):
        self._load_results()
        with open(self.filename, 'w', newline='') as csvfile:
            header = ['Exam Name', 'Number of Candidates', 'Passed', 'Failed', 'Best Score', 'Worst Score']
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            writer.writerow(header)
            for row in self.report.get_rows():
                writer.writerow(row)


report_generator = ExamReportCreator()
report_generator.create()
