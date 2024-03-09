# Written by Wu Juanjuan
# 2023.9

import pymel.core as pm

class UJ2Name:
    def __init__(self):
        if pm.window('UJ2NameWindow', q=1, ex=1):
            pm.deleteUI('UJ2NameWindow')

        # main windowを作る
        self.winUI = pm.window('UJ2NameWindow', title='UJ2Name', menuBar=1, wh=(360,230))
        self.layoutM = pm.columnLayout(adj=1)
        self.layout1 = pm.rowColumnLayout( numberOfColumns=3, columnWidth=[(1, 40), (2, 70), (3, 250)] )
        pm.text('変更')
        self.radioC1 = pm.radioCollection()
        self.radioB1 = pm.radioButton('UJ2Name_Change', l='change', cl=self.radioC1, cc=pm.Callback(self.UiChange))
        self.text1 = pm.textField(en=0)
        pm.setParent('..')

        # change UI
        self.layout1ex = pm.rowColumnLayout( numberOfColumns=4, columnWidth=[(1, 110), (2, 80), (3, 80), (4, 80)] )
        pm.text('')
        self.radioC1ex = pm.radioCollection()
        pm.radioButton('UJ2Name_radioB1ex1', l='選択', cl=self.radioC1ex, en=0)
        pm.radioButton('UJ2Name_radioB1ex2', l='T階層', cl=self.radioC1ex, en=0)
        pm.radioButton('UJ2Name_radioB1ex3', l='D階層', cl=self.radioC1ex, en=0)
        pm.setParent('..')

        # insert UI
        self.layout2 = pm.rowColumnLayout( numberOfColumns=6, columnWidth=[(1, 40), (2, 70), (3, 60), (4, 45), (5, 105), (6, 30)] )
        pm.text('')
        self.radioB2 = pm.radioButton('UJ2Name_Insert', l='insert', cl=self.radioC1, cc=pm.Callback(self.UiChange))
        self.int2 = pm.intField(en=0)
        self.text2ex = pm.textField(tx='_', en=0)
        self.text2 = pm.textField(en=0)
        self.ictxButton201 = pm.iconTextButton(style='iconOnly', image1='TypePivot.png', en=0)
        self.popMenu2 = pm.popupMenu(button=1)
        self.menuIt201 = []
        # プリセット
        self.option2 = ['fk', 'ik', 'dr', 'bnd', 'sk', 'RF']
        for i,opt in enumerate(self.option2):
            self.menuIt201 = pm.menuItem(label=self.option2[i], command=pm.Callback(self.insertUiChange, opt))
        pm.setParent('..')
        
        # insert UI
        self.layout2ex = pm.rowColumnLayout( numberOfColumns=4, columnWidth=[(1, 110), (2, 80), (3, 80), (4, 80)] )
        pm.text('')
        self.radioC2ex = pm.radioCollection()
        pm.radioButton('UJ2Name_radioB2ex1', l='選択', cl=self.radioC2ex, en=0)
        pm.radioButton('UJ2Name_radioB2ex2', l='T階層', cl=self.radioC2ex, en=0)
        pm.radioButton('UJ2Name_radioB2ex3', l='D階層', cl=self.radioC2ex, en=0)
        pm.setParent('..')

        # replace UI
        self.layout3 = pm.rowColumnLayout( numberOfColumns=6, columnWidth=[(1, 40), (2, 70), (3, 105), (4, 105), (5, 20), (6,20)] )
        pm.text('')
        self.radioB3 = pm.radioButton('UJ2Name_Replace', l='replace', cl=self.radioC1, cc=pm.Callback(self.UiChange))
        self.text301 = pm.textField(en=0)
        self.text302 = pm.textField(en=0)

        self.ictxButton301 = pm.iconTextButton(style='iconOnly', image1='TypePivot.png', en=0)
        self.popMenu3 = pm.popupMenu(button=1)
        #self.menuIt301 = []
        # プリセット
        self.option3 = ['_fk_,_ik_', '_L_,_R_', '_ik_,_dr_', '_fk_,_dr_']
        for i,opt in enumerate(self.option3):
            pm.menuItem(label=self.option3[i], command=pm.Callback(self.replaceUiChange, opt))
        
        self.ictxButton302 = pm.iconTextButton(style='iconOnly', image1='SVGRefresh.png', command=pm.Callback(self.replaceUiReverse), en=0)
        pm.setParent('..')

        # replace UI
        self.layout3ex = pm.rowColumnLayout( numberOfColumns=4, columnWidth=[(1, 110), (2, 80), (3, 80), (4, 80)] )
        pm.text('')
        self.radioC3ex = pm.radioCollection()
        pm.radioButton('UJ2Name_radioB3ex1', l='選択', cl=self.radioC3ex, en=0)
        pm.radioButton('UJ2Name_radioB3ex2', l='D階層', cl=self.radioC3ex, en=0)
        pm.radioButton('UJ2Name_radioB3ex3', l='全部', cl=self.radioC3ex, en=0)
        pm.setParent('..')
        
        
        
        pm.button(l='execute',h=40, command=pm.Callback(self.UJ2NameExecute))
    
    
    def showUI(self):
        self.winUI.show()
    
    def closeUI(self):
        self.winUI.close()
        
    def insertUiChange(self, opt):
        self.text2.setText(opt)
    
    def replaceUiChange(self, opt):
        str1, str2 = opt.split(',')
        self.text301.setText(str1)
        self.text302.setText(str2)
    
    def replaceUiReverse(self):
        str1 = self.text302.getText()
        str2 = self.text301.getText()
        self.text301.setText(str1)
        self.text302.setText(str2)
    
    def UiChange(self):
        sel = self.radioC1.getSelect()
        if sel=='UJ2Name_Change' :
            pm.radioButton('UJ2Name_radioB1ex1', e=1, en=1)
            pm.radioButton('UJ2Name_radioB1ex2', e=1, en=1)
            pm.radioButton('UJ2Name_radioB1ex3', e=1, en=1)
            self.text1.setEnable(1)
            
            pm.radioButton('UJ2Name_radioB2ex1', e=1, en=0)
            pm.radioButton('UJ2Name_radioB2ex2', e=1, en=0)
            pm.radioButton('UJ2Name_radioB2ex3', e=1, en=0)
            self.int2.setEnable(0)
            self.text2ex.setEnable(0)
            self.text2.setEnable(0)
            self.ictxButton201.setEnable(0)
            pm.radioButton('UJ2Name_radioB3ex1', e=1, en=0)
            pm.radioButton('UJ2Name_radioB3ex2', e=1, en=0)
            pm.radioButton('UJ2Name_radioB3ex3', e=1, en=0)
            self.text301.setEnable(0)
            self.text302.setEnable(0)
            self.ictxButton301.setEnable(0)
            self.ictxButton302.setEnable(0)
            
        elif sel=='UJ2Name_Insert' :
            pm.radioButton('UJ2Name_radioB2ex1', e=1, en=1)
            pm.radioButton('UJ2Name_radioB2ex2', e=1, en=1)
            pm.radioButton('UJ2Name_radioB2ex3', e=1, en=1)
            self.int2.setEnable(1)
            self.text2ex.setEnable(1)
            self.text2.setEnable(1)
            self.ictxButton201.setEnable(1)
            
            pm.radioButton('UJ2Name_radioB1ex1', e=1, en=0)
            pm.radioButton('UJ2Name_radioB1ex2', e=1, en=0)
            pm.radioButton('UJ2Name_radioB1ex3', e=1, en=0)
            self.text1.setEnable(0)
            pm.radioButton('UJ2Name_radioB3ex1', e=1, en=0)
            pm.radioButton('UJ2Name_radioB3ex2', e=1, en=0)
            pm.radioButton('UJ2Name_radioB3ex3', e=1, en=0)
            self.text301.setEnable(0)
            self.text302.setEnable(0)
            self.ictxButton301.setEnable(0)
            self.ictxButton302.setEnable(0)
        
        elif sel=='UJ2Name_Replace' :
            pm.radioButton('UJ2Name_radioB3ex1', e=1, en=1)
            pm.radioButton('UJ2Name_radioB3ex2', e=1, en=1)
            pm.radioButton('UJ2Name_radioB3ex3', e=1, en=1)
            self.text301.setEnable(1)
            self.text302.setEnable(1)
            self.ictxButton301.setEnable(1)
            self.ictxButton302.setEnable(1)
            
            pm.radioButton('UJ2Name_radioB1ex1', e=1, en=0)
            pm.radioButton('UJ2Name_radioB1ex2', e=1, en=0)
            pm.radioButton('UJ2Name_radioB1ex3', e=1, en=0)
            self.text1.setEnable(0)
            pm.radioButton('UJ2Name_radioB2ex1', e=1, en=0)
            pm.radioButton('UJ2Name_radioB2ex2', e=1, en=0)
            pm.radioButton('UJ2Name_radioB2ex3', e=1, en=0)
            self.int2.setEnable(0)
            self.text2ex.setEnable(0)
            self.text2.setEnable(0)
            self.ictxButton201.setEnable(0)
        

    # 入力文字列の名前部分をゲット
    @staticmethod
    def getAlphabet(input_str, amount):
        num = 0
        # 選択されたオブジェクトの数をゲット
        lenth = len(input_str)
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # 番号の桁をゲット
        for char in input_str[::-1]:
            if char.isdigit():
                num += 1
            # breakがなければ文字列の中の番号以外の数字は影響を受ける
            else : break
        # 入力文字列最後の番号部分を取り除いて名前部分しか残らない
        alp = input_str[:(lenth-num)]
        output_str = ''
        # 27だったら組分けしない
        if amount == 27 :
            output_str = alp
        elif 0 <=amount < 27 :
            output_str = alp + alpha[amount]
        else :
            pm.error('amount out of 26')
        return(output_str)

    # 入力名前の番号をint数字にする
    @staticmethod
    def getNumber(input_str):
        num_str = ''
        num_str_modified = ''
        ipNum_lenth = 1
        # num_lenth = 1
        number = 0
        # 番号の文字列をゲット
        for char in input_str[::-1]:
            if char.isdigit():
                num_str += char
            # breakがなければ文字列の中の番号以外の数字に影響される
            else : break
        # 数字の順番を修正する
        for char in range(len(num_str)):
            num_str_modified += num_str[-1-char]
        # 正しいint数字と桁数をゲット
        if num_str:
            ipNum_lenth = len(num_str_modified)
            number = int(num_str_modified, 10)
        return([number, ipNum_lenth])

    # リネームのための番号リストをゲット
    @staticmethod
    def getSerialNumber(number, ipNum_lenth, obj_lenth):
        # 数字リストをゲット
        serialNumber = [ (number+n) for n in range(obj_lenth) ]
        # 番号リストは修正された数字リストです
        modified_serialNumber = []
        
        # 番号に0は必要かどうかを判断する
        # 三桁まで。桁を増やしてもいいが
        if ipNum_lenth == 1 :
            modified_serialNumber = [ str(n) for n in serialNumber ]
        elif ipNum_lenth == 2 :
            for n in serialNumber:
                if 0 <= n < 10 :
                    modified_serialNumber.append('0'+str(n))
                else:
                    modified_serialNumber.append(str(n))
        elif ipNum_lenth == 3 :
            for n in serialNumber:
                if 0 <= n < 10 :
                    modified_serialNumber.append('00'+str(n))
                elif 10 <= n < 100 :
                    modified_serialNumber.append('0'+str(n))
                elif n >= 100 :
                    modified_serialNumber.append(str(n))
        return(modified_serialNumber)
    
    # namefieldやオブジェクト本当の名前をゲット
    @staticmethod
    def dealWithNameField(obj):
        namefieldList = obj.split('|')
        namefield = ('|').join(namefieldList[0:-1])
        if namefield :
            namefield += '|'
        obj_name = namefieldList[-1]
        # 例 A|B|C|objName  [objName, A|B|C|, [A, B, C, objName]]
        return([obj_name, namefield, namefieldList])
    
    # namespaceやオブジェクト本当の名前をゲット
    @staticmethod
    def dealWithNameSpace(obj):
        # namespaceを処理する前に、namefieldを引き離さなければならない
        obj_name_nonf, namefield, namefieldList = UJ2Name.dealWithNameField(obj)
        obj_name = ''
        namespace = ''
        namespaceList = []
        # オブジェクトの名前にnamespaceの存在するかしないかをチェック
        checkNs = ':' in obj_name_nonf
        if checkNs == 1 :
            namespaceList = obj_name_nonf.split(':')
            obj_name = namespaceList[-1]
            namespace = (':').join(namespaceList[0:-1]) + ':'
        else :
            obj_name = obj_name_nonf
            namespaceList = [namespace, obj_name]
        # 例 A:B:C:objName  [objName, A:B:C:, [A, B, C, objName]]
        return([obj_name, namespace, namespaceList])
    
    # 同じ名前を避けるために
    # リネームしたいオブジェクトが一つしかない時に使うもの。ほぼほかのツールのためのコード
    @staticmethod
    def reSingleName(obj, new_str):
        # 影響をなくすためにnamespaceをrootに
        pm.namespace( set = ':' )
        # オブジェクトのnamespaceをチェック
        obj_name, namespace, namespaceList = UJ2Name.dealWithNameSpace(obj)
        if namespace : new_str = namespace + new_str
        # 新しい名前の名前部分をゲット
        alphabet = UJ2Name.getAlphabet(new_str, amount=27)
        # 新しい名前の番号部分をゲット
        input_number = UJ2Name.getNumber(new_str)
        if pm.objExists(new_str) == 0 :
                pm.rename(obj, new_str)
        elif obj == pm.PyNode(new_str) :
            pass
        # 同じ名前のオブジェクトがあるとき、番号+1
        else:
            for i in range(10000):
                output_number = 1 + i + int(input_number[0])
                output_number_len = len(str(output_number))
                mul = input_number[1] - output_number_len
                if mul > 0 :
                    fore = '0'*mul
                    modified_str = alphabet + fore + str(output_number)
                else :
                    modified_str = alphabet + str(output_number)
                
                # 同じ名前のオブジェクトは指定したオブジェクト自分自身の場合
                if str(obj) == modified_str :
                    break
                elif pm.objExists(modified_str) == 0 :
                    pm.rename(obj, modified_str)
                    break
                else :
                    continue

    # 複数のオブジェクトをリネーム
    @staticmethod
    def reSerialName(selChain, new_str, amount):
        # もしSerialAlphaが必要ないなら、 amount = int 27
        # 影響をなくすためにnamespaceをrootに
        pm.namespace( set = ':' )
        # オブジェクト数をゲット
        obj_lenth = len(selChain)
        # 新しい名前の名前部分をゲット
        alphabet = UJ2Name.getAlphabet(new_str, amount)
        # 新しい名前の番号部分をゲット
        input_number = UJ2Name.getNumber(new_str)
        # すべてのオブジェクトの新しい名前の番号リストをゲット
        serial_number = UJ2Name.getSerialNumber(input_number[0], input_number[1], obj_lenth)
        # リネーム
        for num, obj in enumerate(selChain):
            # namespaceをチェック
            obj_name, namespace, namespaceList = UJ2Name.dealWithNameSpace(obj)
            if namespace :
                new_serialName = namespace + alphabet + serial_number[num]
            else :
                new_serialName = alphabet + serial_number[num]
            
            if pm.objExists(new_serialName) == 0 :
                pm.rename(obj, new_serialName)
            elif str(obj) == new_serialName :
                continue
            else:
                pm.error(new_serialName+'_objExists')
                
    
    @staticmethod
    def insertStr(position, prefix, insert_string, originalname):
        # ここprefix実はseparatorという意味をしている
        # 影響をなくすためにnamespaceをrootに
        pm.namespace( set = ':' )
        # namefieldをチェック
        obj_name_nonf, namefield, namefieldList = UJ2Name.dealWithNameField(originalname)
        # namespaceをチェック
        obj_name_nonfns, namespace, namespaceList = UJ2Name.dealWithNameSpace(obj_name_nonf)
        # 区切り記号を取り除く
        name_list = [ str(x) for x in obj_name_nonfns.split(prefix) ]
        name_list.insert(position, insert_string)
        if namefield :
            if namespace :
                modified_string = namefield + namespace + (prefix.join(name_list))
            else :
                modified_string = namefield + (prefix.join(name_list))
        else :
            if namespace :
                modified_string = namespace + (prefix.join(name_list))
            else:
                modified_string = prefix.join(name_list)
        # リネーム
        if pm.objExists(modified_string)==0 :
            pm.rename(originalname, modified_string)
        else:
            pm.error(modified_string+'_objExists')
        
    @staticmethod
    def replaceName(str1, str2, sel):
        how = ['selected', 'hierarchy', 'all']
        # 置換機能はMAYAの標準機能を取り込むもの
        # 少し思うところもあるだがまた暇の時に書く
        pm.mel.searchReplaceNames(str1, str2, how[sel-1])

    # 新たな機能、未完成
    @staticmethod
    def addNamespace(selChain, ns, parent=':'):
        pm.namespace(add=ns, parent=parent)
        for obj in selChain :
            new_Name = ns + ':' + str(obj)
            if pm.objExists(new_Name) == 0 :
                pm.rename(obj, new_Name)
            else:
                pm.error(new_Name+'_objExists')


    def UJ2NameExecute(self):
        sel = self.radioC1.getSelect()
        # 名前変更を実行
        if sel=='UJ2Name_Change' :
            selected_obj = pm.selected()
            # 選択したオブジェクトの数をゲット
            lenth = len(selected_obj)
            new_str = self.text1.getText()
            rc2_opt = int(self.radioC1ex.getSelect()[-1])
            # 選択オプション
            if rc2_opt == 1 :
                if lenth == 1 :
                    UJ2Name.reSingleName(selected_obj[0], new_str)
                elif lenth > 1 :
                    # オブジェクトは一つ以上の場合
                    # If there is no SerialAlpha needed, int 27 should be written in amount.
                    UJ2Name.reSerialName(selected_obj, new_str, amount=27)
                else :
                    pass
            # T階層オプション
            elif rc2_opt == 2 :
                for amount, o in enumerate(selected_obj):
                    selChain = UJ2Select.getTypeHierarchy(o)
                    if lenth > 1 :
                        UJ2Name.reSerialName(selChain, new_str, amount)
                    elif lenth == 1 :
                        UJ2Name.reSerialName(selChain, new_str, amount=27)
                    else :
                        pass
            # D階層オプション
            elif rc2_opt == 3 :
                for amount, o in enumerate(selected_obj):
                    selChain = UJ2Select.getDagHierarchy(o)
                    if lenth > 1 :
                        UJ2Name.reSerialName(selChain, new_str, amount)
                    elif lenth == 1 :
                        UJ2Name.reSerialName(selChain, new_str, amount=27)
                    else :
                        pass
            else :
                pass
        
        # 文字挿入を実行
        elif sel=='UJ2Name_Insert' :
            position = self.int2.getValue()
            insert_string = self.text2.getText()
            prefix = self.text2ex.getText()
            
            rc2_opt = int(self.radioC2ex.getSelect()[-1])
            # 選択オプション
            if rc2_opt == 1 :
                obj = pm.selected()
                for o in obj:
                    UJ2Name.insertStr(position, prefix, insert_string, o)
            # T階層オプション        
            elif rc2_opt == 2 :
                selected_obj = pm.selected()
                for obj in selected_obj :
                    obj_typeHierarchy = UJ2Select.getTypeHierarchy(obj)
                    for o in obj_typeHierarchy :
                        UJ2Name.insertStr(position, prefix, insert_string, o)
            # D階層オプション  
            elif rc2_opt == 3 :
                selected_obj = pm.selected()
                for obj in selected_obj :
                    obj_dagHierarchy = UJ2Select.getDagHierarchy(obj)
                    for o in obj_dagHierarchy :
                        UJ2Name.insertStr(position, prefix, insert_string, o)
            else :
                pass
            
        # 文字置換を実行
        elif sel=='UJ2Name_Replace' :
            sel = int(self.radioC3ex.getSelect()[-1])
            str1 = self.text301.getText()
            str2 = self.text302.getText()
            UJ2Name.replaceName(str1, str2, sel)
        
        else :
            pass



class UJ2Select:

    # 選択したオブジェクトと、指定したノードタイプの子どもをゲット
    @staticmethod
    def SpecifiedTypeHierarchy(sel, Ntype):
        # sel = pm.selected()[0]
        selChain = [ child for child in (sel.listRelatives(ad=1, c=1))[::-1] if (pm.nodeType(child))==Ntype ]
        selChain.insert(0, sel)
        return(selChain)

    # 選択したオブジェクトと、それと同じノードタイプの子どもをゲット
    @staticmethod
    def getTypeHierarchy(sel):
        # sel = pm.selected()[0]
        Ntype = pm.nodeType(sel)
        selChain = [ child for child in (sel.listRelatives(ad=1, c=1))[::-1] if (pm.nodeType(child))==Ntype ]
        selChain.insert(0, sel)
        return(selChain)

    # 選択したオブジェクトと、それと同じノードタイプの全部の親をゲット
    @staticmethod
    def getTypeHierarchy_r(sel):
        # sel = pm.selected()[0]
        Ntype = pm.nodeType(sel)
        chain = []
        p = sel.listRelatives(p=1)[0]
        while p:
            chain.append(p)
            try :
                p = p.listRelatives(p=1)[0]
            except : break
        selChain = [ parent for parent in reversed(chain) if (pm.nodeType(parent))==Ntype ]
        selChain.append(sel)
        return(selChain)

    # 選択したオブジェクトと、Dagノードの子どもをゲット
    @staticmethod
    def getDagHierarchy(sel):
        selChain = [ child for child in (sel.listRelatives(ad=1, c=1))[::-1] ]
        selChain.insert(0, sel)
        shape = pm.ls(selChain, s=1)
        for s in shape:
            selChain.remove(s)
        return(selChain)
        
    @staticmethod
    def getDagHierarchy_r(sel):
        # sel = pm.selected()[0]
        # Ntype = pm.nodeType(sel)
        chain = []
        p = sel.listRelatives(p=1)[0]
        while p:
            chain.append(p)
            try :
                p = p.listRelatives(p=1)[0]
            except : break
        selChain = [ parent for parent in reversed(chain) ]
        selChain.append(sel)
        shape = pm.ls(selChain, s=1)
        for s in shape:
            selChain.remove(s)
        return(selChain)

    # シェイプノード含み
    @staticmethod
    def getAllHierarchy(sel):
        selChain = [ child for child in (sel.listRelatives(ad=1, c=1))[::-1] ]
        selChain.insert(0, sel)
        return(selChain)


if __name__ == '__main__':
    n = UJ2Name()
    n.showUI()

