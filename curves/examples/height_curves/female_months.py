class HeightCurveFemaleMonths(object):
    """
    Height-based growth curve for females aged 0 to 36 months
    """

    def __init__(self):
        """
        Growth curve based on the height of female children with Down Syndrome
        constructor.
        """

        self.title = "Height-based growth curve for females aged 0 to 36 months"

        self.ages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                     18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                     33, 34, 35, 36]

        self.percentis_3 = [41.54, 44.24, 46.88, 49.40, 51.74, 53.89, 55.84, 57.60,
                            59.18, 60.60, 61.90, 63.08, 64.18, 65.20, 66.17, 67.09,
                            67.96, 68.80, 69.61, 70.38, 71.13, 71.84, 72.53, 73.20,
                            73.85, 74.49, 75.11, 75.72, 76.32, 76.91, 77.49, 78.08,
                            78.65, 79.23, 79.79, 80.36, 80.92]

        self.percentis_10 = [43.84, 46.51, 49.13, 51.62, 53.94, 56.07, 58.00, 59.73,
                             61.29, 62.69, 63.96, 65.13, 66.21, 67.23, 68.19, 69.10,
                             69.98, 70.82, 71.64, 72.43, 73.19, 73.92, 74.64, 75.33,
                             76.01, 76.68, 77.33, 77.98, 78.62, 79.25, 79.88, 80.51,
                             81.13, 81.76, 82.38, 82.99, 83.60]

        self.percentis_25 = [45.87, 48.57, 51.21, 53.73, 56.06, 58.19, 60.12, 61.85,
                             63.40, 64.79, 66.06, 67.22, 68.29, 69.30, 70.26, 71.18,
                             72.06, 72.91, 73.74, 74.54, 75.31, 76.07, 76.80, 77.52,
                             78.23, 78.92, 79.60, 80.28, 80.94, 81.61, 82.27, 82.93,
                             83.58, 84.24, 84.89, 85.54, 86.19]

        self.percentis_50 = [47.70, 50.46, 53.16, 55.72, 58.10, 60.26, 62.21, 63.95,
                             65.51, 66.91, 68.17, 69.34, 70.41, 71.42, 72.39, 73.31,
                             74.20, 75.06, 75.90, 76.72, 77.51, 78.28, 79.03, 79.77,
                             80.49, 81.21, 81.91, 82.60, 83.29, 83.97, 84.65, 85.33,
                             86.00, 86.68, 87.35, 88.01, 88.68]

        self.percentis_75 = [49.37, 52.22, 54.99, 57.63, 60.06, 62.27, 64.26, 66.04,
                             67.62, 69.04, 70.32, 71.49, 72.58, 73.60, 74.57, 75.51,
                             76.41, 77.28, 78.14, 78.97, 79.77, 80.56, 81.33, 82.08,
                             82.82, 83.54, 84.26, 84.96, 85.65, 86.34, 87.03, 87.71,
                             88.39, 89.07, 89.75, 90.42, 91.09]

        self.percentis_90 = [50.91, 53.85, 56.73, 59.45, 61.96, 64.24, 66.29, 68.12,
                             69.74, 71.18, 72.49, 73.68, 74.79, 75.83, 76.81, 77.76,
                             78.68, 79.57, 80.44, 81.29, 82.11, 82.91, 83.69, 84.45,
                             85.20, 85.93, 86.64, 87.35, 88.04, 88.73, 89.40, 90.08,
                             90.76, 91.43, 92.09, 92.76, 93.42]

        self.percentis_97 = [52.34, 55.39, 58.37, 61.20, 63.80, 66.17, 68.29, 70.18,
                             71.85, 73.34, 74.69, 75.91, 77.05, 78.11, 79.12, 80.09,
                             81.03, 81.94, 82.83, 83.69, 84.53, 85.34, 86.13, 86.89,
                             87.64, 88.37, 89.08, 89.77, 90.45, 91.12, 91.78, 92.44,
                             93.09, 93.75, 94.39, 95.04, 95.69]

    def make(self):
        """
        Get the values to make the chart
        """

        return {
            'ages': self.ages,
            'title': self.title,
            'percentis_3': self.percentis_3,
            'percentis_10': self.percentis_10,
            'percentis_25': self.percentis_25,
            'percentis_50': self.percentis_50,
            'percentis_75': self.percentis_75,
            'percentis_90': self.percentis_90,
            'percentis_97': self.percentis_97
        }
