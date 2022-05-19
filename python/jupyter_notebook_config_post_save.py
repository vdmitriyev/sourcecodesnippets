################################################
#
# Own hooks
#
################################################

c = get_config()

def post_save(model, os_path, contents_manager):
    '''Post-save hook to automatically convert notebooks to .py scripts and .html files
       Base on the : https://github.com/ipython/ipython/issues/8009
    '''

    import os
    import shutil

    from subprocess import check_call
    from datetime import datetime

    if model['type'] != 'notebook':
        return # only do this for notebooks

    def convert_and_copy(target_format, os_path):
        '''Convert and copy'''

        if target_format not in ['html', 'py']:
            print('[x] Wrong format for conversion')
            return

        d, fname = os.path.split(os_path)
        fname_target = f'{fname[:-6]}.{target_format.lower()}'
        dir_target = os.path.join(d, target_format.upper())
        if not os.path.exists(dir_target):
            os.makedirs(dir_target)
        check_call(['jupyter', 'nbconvert', '--to', 'html', fname], cwd=d)
        shutil.move(os.path.join(d, fname_target), os.path.join(dir_target, fname_target))
        print(f'{datetime.now()} save into {os.path.join(dir_target, fname_target)}')

    convert_and_copy(target_format='html', os_path=os_path)
    convert_and_copy(target_format='py', os_path=os_path)

c.FileContentsManager.post_save_hook = post_save
