from viewer import Viewer


def main():
    viewer = Viewer()
    viewer.ask_file_name()
    if (viewer.file_name):
        viewer.test_begin()
        viewer.testing()
        viewer.test_end()
        viewer.print_result_test()


if __name__ == '__main__':
    main()
