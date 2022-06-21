from imblearn.over_sampling import RandomOverSampler


def Ros(data, label):
    ros = RandomOverSampler(random_state=0)
    data_ros, label_ros = ros.fit_sample(data, label)
    print(data_ros)


if __name__ == '__main__':
    Ros()