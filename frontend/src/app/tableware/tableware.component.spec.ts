import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TablewareComponent } from './tableware.component';

describe('tablewareComponent', () => {
  let component: TablewareComponent;
  let fixture: ComponentFixture<TablewareComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TablewareComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TablewareComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
