#!/usr/bin/python3
import os
import subprocess

class Color:
 RED = '\033[91m'
 GREEN = '\033[92m'
 YELLOW = '\033[93m'
 LAVENDER = '\033[94m'

class ComponentCLI:

    def printColor(s, color):
        """ Prints color to terminal. """
        print('{} {}\033[00m'.format(color, s))
        
    name_list = []
	    
    def main():
        ComponentCLI.printColor('---------------------------------------------------------------------------------', Color.LAVENDER)

        ComponentCLI.printColor('Welcome to the React-Skeleton New Component Generator!', Color.GREEN)
        ComponentCLI.printColor('This is where you will make decisions about your new component.', Color.GREEN)
        ComponentCLI.printColor('Don\'t worry, though. You can always change things later.', Color.LAVENDER)

        ComponentCLI.printColor('---------------------------------------------------------------------------------', Color.LAVENDER)
        name = ''
        ComponentCLI.assign_name(name)
        print("Name: " + name)
        
        ComponentCLI.printColor('---------------------------------------------------------------------------------', Color.LAVENDER)

        ComponentCLI.printColor('By default, your new component will extend only the base component.', Color.YELLOW)
        print('If you would like to extend another')
        filepath = str(input('enter the path --TO THE PARENT DIRECTORY-- here: [Skip]'))
        
        if filepath != '':
            return ComponentCLI.execute_call(name, filepath)
        
        ComponentCLI.printColor('---------------------------------------------------------------------------------', Color.LAVENDER)
        
        base_list = os.listdir('./components')
        for item in base_list:
            if not '.' in item and not '_' in item:
                ComponentCLI.built_in_list.append(item)
        print('If you would like to extend one of React-Skeleton\'s included components, select one here: ')
        
        return ComponentCLI.selector(ComponentCLI.counter)
        
    built_in_list = []
    noList = []
    counter = 0
    
    def selector(counter):
        listLimiter = 8
        inheritance_list = []
        root_path = 'components/'
        selector = str(input(ComponentCLI.built_in_list[ComponentCLI.counter] + ': Y/n [n]'))
        if selector == 'Y' or selector == 'y':
            inheritance_list.append(root_path + ComponentCLI.built_in_list[ComponentCLI.counter])
            filepath = inheritance_list[counter]
        else:
            ComponentCLI.noList.append('no')
        if len(ComponentCLI.noList) > 7:
            
            return ComponentCLI.execute_call(name, filepath)
        if len(inheritance_list) > 0:
        
            return ComponentCLI.execute_call(name, filepath)
        else:
            ComponentCLI.counter += 1
            ComponentCLI.selector(counter)
        
    def execute_call(name, filepath):
        ComponentCLI.subprocess.call(['./create_component.sh', name,  filepath])
        
        return print('If all went well, your new component will be in ./src/components/<your-new-compponent>')
       
    def assign_name(name_list):
        name = str(input('What do you want to call your new component? [GenericComponent]'))
        if ' ' in name:
            print('Component names cannot contain spaces.')
            ComponentCLI.assign_name(name_list)
        if name == '':
            name = 'GenericComponent'
        return name
